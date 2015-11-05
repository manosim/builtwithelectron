{% block subject %}Your submission to Built with Electron got approved.{% endblock %}

{% block body %}
Dear {{ user.username }},

Your submission {{ entry.name }} got approved and now shows up at Built with Electron!

Visit Built with Electron at {{ site_url }}{% url 'directory:detail' entry.slug %} to view your submission.

Best regards,

Built with Electron.
{% endblock %}

{% block html %}
<p>Dear {{ user.username }},</p>

<p>Your submission {{ entry.name }} got approved and now shows up at Built with Electron!</p>

<p>Visit Built with Electron at <a href="{{ site_url }}{% url 'directory:detail' entry.slug %}">{{ site_url }}{% url 'directory:detail' entry.slug %}</a> to view your submission.</p>

<p>Best regards,</p>

<p>Built with Electron.</p>
{% endblock %}
