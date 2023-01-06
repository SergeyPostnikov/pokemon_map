import folium
from django.utils.timezone import localtime
import json
from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
        )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    time_now = localtime()
    pokemons = Pokemon.objects.all()
    pokemon_entities = PokemonEntity.objects.filter(
        appeared_at__lte=time_now,
        disappeared_at__gt=time_now
        )

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon_entities:    
        add_pokemon(
            folium_map, pokemon_entity.latitude,
            pokemon_entity.longitude,
            request.build_absolute_uri(pokemon_entity.kind.image.url)
        )

    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': request.build_absolute_uri(pokemon.image.url),
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    time_now = localtime()
    pokemon = Pokemon.objects.get(id=pokemon_id)
    pokemon_entities = PokemonEntity.objects.filter(
        kind=pokemon,
        appeared_at__lte=time_now,
        disappeared_at__gt=time_now
        )

    pokemon_wrapper = {
        'img_url': request.build_absolute_uri(pokemon.image.url),
        'title_ru': pokemon.title,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
        'description': pokemon.description
    }

    pokemon_evolution = pokemon.previous_evolution
    if pokemon_evolution:    
        pokemon_wrapper['previous_evolution'] = {
            'img_url': request.build_absolute_uri(pokemon_evolution.image.url),
            'title_ru': pokemon_evolution.title,
            'pokemon_id': pokemon_evolution.id
        }

    # pokemon_evolution = Pokemon.objects.filter(previous_evolution=pokemon).first()
    try:
        pokemon_evolution = pokemon.next_evolutions.get()
    except Pokemon.DoesNotExist:
        pokemon_evolution = None
        
    if pokemon_evolution:    
        pokemon_wrapper['next_evolution'] = {
            'img_url': request.build_absolute_uri(pokemon_evolution.image.url),
            'title_ru': pokemon_evolution.title,
            'pokemon_id': pokemon_evolution.id
        }

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map, pokemon_entity.latitude,
            pokemon_entity.longitude,
            request.build_absolute_uri(pokemon.image.url)
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_wrapper
    })
