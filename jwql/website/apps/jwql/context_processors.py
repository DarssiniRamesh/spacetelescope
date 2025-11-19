"""Provides functions that define context inherent to all views.

The functions within this module define ``context`` that will be
included in requests, in addition to any specific ``context`` provided
in the view.

Authors
-------

    - Matthew Bourque

Use
---

    This module is defined under the ``TEMPLATES.OPTIONS`` setting in
    ``settings.py``, e.g.:
    ::

        TEMPLATES = [
            {'OPTIONS': {'context_processors': ['jwql.website.apps.jwql.context_processors.base_context'],},}
        ]

    As such, it will automatically be executed upon each request.
"""

import bokeh

import jwql
from jwql.utils.constants import JWST_INSTRUMENT_NAMES, MONITORS, URL_DICT

# Defensive fallback: If JWST_INSTRUMENT_NAMES does not include all expected instruments,
# define a robust function to always provide the core set. This prevents homepage failures.
DEFAULT_INSTRUMENTS = ['niriss', 'nircam', 'nirspec', 'miri', 'fgs']

def get_instruments_safe():
    """Return a robust list of instrument names, always including core JWST instruments."""
    try:
        # If present and non-empty, return the constant (with all required instruments)
        instruments = list(JWST_INSTRUMENT_NAMES)
        if instruments and isinstance(instruments, (list, tuple)):
            for core in DEFAULT_INSTRUMENTS:
                if core not in instruments:
                    instruments.append(core)
            return instruments
    except Exception:
        pass
    return DEFAULT_INSTRUMENTS

# PUBLIC_INTERFACE
def base_context(request):
    """Provide the context needed for the ``base.html`` template.

    Parameters
    ----------
    request : HttpRequest object
        Incoming request from the webpage

    Returns
    -------
    context : dict
        A dictionary containing data needed to render the ``base.html``
        template
    """

    context = {}
    # Use a robust helper to always provide valid instruments list
    context['inst_list'] = get_instruments_safe()
    context['tools'] = MONITORS
    context['version'] = getattr(jwql, "__version__", "dev")
    context['bokeh_version'] = getattr(bokeh, "__version__", "unknown")
    context['url_dict'] = URL_DICT

    return context
