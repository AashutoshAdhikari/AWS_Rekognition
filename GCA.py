import boto3
import json
from tabulate import tabulate

rekognition_client=boto3.client('rekognition')
for file in ('aashutosh.jpg','amit.jpg','nani.jpg','jeff.jpg'):
    print('')
    print(file)
    file = open(file,'rb').read()
    response = rekognition_client.detect_faces(
        Image = {
            'Bytes': file
        },
        Attributes = ['ALL']
    )
    for face in response['FaceDetails']:
        print('The candidate is aged between ' + str(face['AgeRange']['Low']) + ' and ' + str(face['AgeRange']['High']))
        print('The candidate is ' + str(face['Gender']['Value']))

        if str(face['Gender']['Value']) == 'Male':
            beard = str(face['Beard']['Value'])
            if beard == 'True':
                print('The male candidate has beard.')
            else:
                print('The male candidate doesn\'t have beard.')
            moustache = str(face['Mustache']['Value'])
            if moustache == 'True':
                print('The male candidate has moustache.')
            else:
                print('The male candidate doesn\'t have moustache.')
        for emotion in face['Emotions']:
            if (emotion['Confidence'] > 70):
                print('The person is {} with confidence of {}'.format(emotion['Type'],emotion['Confidence']))

        eyeglass = str(face['Eyeglasses']['Value'])
        if eyeglass == 'True':
            print('The candidate wears eyeglasses.')
        else:
            print('The candidate doesn\'t wear eyeglasses.')
