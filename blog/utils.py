import json

from pathlib import Path
from typing import Any, Dict, List, Union

from django.conf import settings
from django.template.loader import render_to_string
def render_to_file(
    template_name: str,
    target_dir: Path,
    context: Dict[str, Any],
    encoding: str = 'utf-8'
) -> str:
    """Renders html template from django template to html file.

    Args:
        template_name (str): name of django template that lies in templates
                             folder, ie 'index.html' or 'iter1/src/index.html'
        target_dir (Path): Path-object to directory to which template should be
                           rendered, ie BASE_DIR / 'templates' / 'rendered'
        context (dict): Context for django-template.
        encoding (str): encoding to use for rendered templates,
                        utf-8 by default.

    Returns:
        result_path (str): path to rendered html-template.

    Raises:
        ValueError: if template_name points to non-existing template.
    """

    src_template_path = settings.TEMPLATES_DIR / template_name
    if not src_template_path.is_file():
        raise ValueError(
            'Path to source template is incorrect or file does not exist!'
        )

    if not target_dir.exists():
        target_dir.mkdir(parents=True)

    rendered_template_path = target_dir / src_template_path.name

    rendered_template_string: str = ''
    try:
        rendered_template_string = render_to_string(template_name, context)
    except Exception as err:
        print(
            'An exception has occured, during template rendering:',
            err,
            sep='\n'
        )

    rendered_template_path.write_text(
        rendered_template_string,
        encoding=encoding
    )
    return str(rendered_template_path)
