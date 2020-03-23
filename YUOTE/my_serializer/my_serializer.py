from rest_framework import serializers
class CompanySerializer(serializers.Serializer):
    # 1.如果没有source引入models的字段名，序列化字段名必须同models的字段名
    # 2.如果有source引入models的字段名，序列化字段名必须不同于models的字段名，目的是对外隐藏数据库的字段名
    id = serializers.IntegerField()
    company_name = serializers.CharField( )
