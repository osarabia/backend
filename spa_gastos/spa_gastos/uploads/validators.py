from rest_framework import serializers

CONTENT_TYPES = set(['application/vnd.ms-excel'])

def validating_file(tmp_file):
    if tmp_file.size > 2621440:
        raise serializers.ValidationError('size should not exceed 2.5 MB')

    if tmp_file.content_type not in CONTENT_TYPES:
        raise serializers.ValidationError('invalid content type %s' % (tmp_file.content_type))
