# jinjalint

A prototype linter which checks the indentation and the correctness of
[Jinja][jinja]-like/HTML templates. Can [fix issues][django-commit].

It works with [Django’s templates][djangotemplates] too, it should
work with [Twig](https://twig.symfony.com/) and similar template languages.

This linter parses both HTML and Jinja tags and will report mismatched
tags and indentation errors:

```html+jinja
<div>
    {% if something %}
    </div>
{% endif %}
```

```html+jinja
<div>
    <span>
    </div>
</span>
```

```html+jinja
  {% if something %}
 <div> not indented properly
      </div>
   {% endif %}
```

```html+jinja
{% if something %}<a href="somewhere">{% endif %}
    <p>something</p>
{% if not something %}</a>{% endif %}
```

## Usage

Install it with `pip install jinjalint` (or `pip3 install jinjalint` if you are using Python v.3.x), then run it with:

```sh
$ jinjalint template-directory/
```

…or:

```sh
$ jinjalint some-file.html some-other-file.html
```

This is a work in progress. Feel free to contribute :upside_down_face:

[jinja]: http://jinja.pocoo.org/docs/2.9/
[django-commit]: https://github.com/django/djangoproject.com/commit/14a964d626196c857809d9b3b492ff4cfa4b3f40
[djangotemplates]: https://docs.djangoproject.com/en/1.11/ref/templates/language/
