"""
https://medium.com/@chamakhabdallah8/how-to-deploy-a-keras-model-to-production-with-django-drf-celery-and-redis-df4901014355
"""

import time
from .celery import app
from .models import InferenceModel

@app.task(bind=True)
def run_inference(self, inference_id):
    #TODO инференс вписывать здесь
    # prediction = model.predict()
    
    inference_obj = InferenceModel.objects.get(id=inference_id)
    inference_obj.task_id = self.request.id
    inference_obj.save()
    
    time.sleep(3)
    print("Sleep1")
    time.sleep(3)
    print("Sleep2")
    pass