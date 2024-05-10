from rest_framework import serializers
from .models import *
from rest_framework.validators import ValidationError

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"

class TechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technician
        fields = "__all__"

class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genres = GenreSerializer(many=True)
    technicians = TechnicianSerializer(many=True)

    class Meta:
        model = Movie
        fields = "__all__"

    def create(self, validated_data):
        actors_data = validated_data.pop('actors')
        genres_data = validated_data.pop('genres')
        technicians_data = validated_data.pop('technicians')

        movie = Movie.objects.create(**validated_data)

        for actor_data in actors_data:
            actor, _ = Actor.objects.get_or_create(**actor_data)
            movie.actors.add(actor)

        for genre_data in genres_data:
            genre, _ = Genre.objects.get_or_create(**genre_data)
            movie.genres.add(genre)

        for technician_data in technicians_data:
            technician, _ = Technician.objects.get_or_create(**technician_data)
            movie.technicians.add(technician)

        return movie

    def update(self, instance, validated_data):
        actors_data = validated_data.pop('actors', [])
        genres_data = validated_data.pop('genres', [])
        technicians_data = validated_data.pop('technicians', [])

        instance.actors.clear()
        for actor_data in actors_data:
            actor, _ = Actor.objects.get_or_create(**actor_data)
            instance.actors.add(actor)

        instance.genres.clear()
        for genre_data in genres_data:
            genre, _ = Genre.objects.get_or_create(**genre_data)
            instance.genres.add(genre)

        instance.technicians.clear()
        for technician_data in technicians_data:
            technician, _ = Technician.objects.get_or_create(**technician_data)
            instance.technicians.add(technician)

        instance.name = validated_data.get('name', instance.name)
        instance.year = validated_data.get('year', instance.year)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()

        return instance