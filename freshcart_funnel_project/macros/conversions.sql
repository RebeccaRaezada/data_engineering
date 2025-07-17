{% macro conversion_rate(numerator, denominator) %}
    case when {{ denominator }} = 0 then null
         else round({{ numerator }} * 100.0 / {{ denominator }}, 2)
    end
{% endmacro %}
