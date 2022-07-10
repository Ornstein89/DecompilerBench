from rest_framework import serializers
from .models import InferenceModel
from .tasks import run_inference

class InferenceSerializer(serializers.ModelSerializer):
    class Meta : 
        model = InferenceModel
        fields = ('name','result')
        
    def create(self,validated_data):
        name = validated_data.get('name')
        image = validated_data.get('image')
        inference_obj = InferenceModel.objects.create(name=name, image=image) # or simply Inference.objects.create(**validated_data)
        run_infernece.delay(inference_obj.id) # run inference async        
        return inference_obj