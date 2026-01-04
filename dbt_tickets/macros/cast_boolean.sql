{% macro cast_boolean(expression) %}
    ({{ expression }})::boolean
{% endmacro %}
