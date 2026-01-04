{% macro cast_int(expression) %}
    ({{ expression }})::int
{% endmacro %}
