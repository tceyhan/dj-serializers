from rest_framework import serializers 
from .models import Student, Path
from django.utils.timezone import now 
 
''' class StudentSerializer(serializers.Serializer): 
    first_name = serializers.CharField(max_length=30) 
    last_name = serializers.CharField(max_length=30) 
    number = serializers.IntegerField(required=False) 
     
    # If your object instances correspond to Django models you'll also want to ensure that these methods save the object to the database. 
    def create(self, validated_data): 
        return Student.objects.create(**validated_data) 
 
    def update(self, instance, validated_data): 
        instance.first_name = validated_data.get('first_name',instance.first_name) 
        instance.last_name = validated_data.get('last_name', instance.last_name) 
        instance.number = validated_data.get('number', instance.number) 
        instance.save() 
        return instance '''

#! ikinci yöntem 

class StudentSerializer(serializers.ModelSerializer):
    path = serializers.StringRelatedField() 
    days_since_joined = serializers.SerializerMethodField()
    class Meta:
        model = Student
        # fields = ('id', 'first_name', 'last_name', 'number', 'days_since_joined')
        fields = '__all__'
        # exclude = ('id',)

    def validate_first_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Isminiz 3 karakterden kucuk olamaz")
        
    def validate_number(self, value): 
        if value > 1000: 
            raise serializers.ValidationError("Student numberneed to be below 1000") 
            return value

    def get_days_since_joined(self, obj): 
        return (now() - obj.register_date).days

class PathSerializer(serializers.ModelSerializer):
    students = serializers.StringRelatedField(many=True)
    # students = StudentSerializer(many=True) 
    # students = serializers.PrimaryKeyRelatedField(read_only=True, many=True) 
    class Meta: 
        model = Path 
        # fields = ["id", "path_name"]
        fields = '__all__'



    # students = StudentSerializer(many=True, read_only=True) #*tüm bilgiler gelir
    #students = serializers.StringRelatedField(many=True) #* modelde yapılan str methodu görünür.
    #students = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #* modelde yapılan path_name field ve id gösterir