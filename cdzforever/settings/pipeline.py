PIPELINE_CSS = {
    'style': {
        'source_filenames': (
            'less/site.less',
        ),

        'output_filename': 'css/site.min.css',
        'extra_context': {
            'title': 'default',
            'media': '',
        },
    },
}


PIPELINE_JS = {
    'script': {
        'source_filenames': (
            'coffee/site.coffee',
        ),

        'output_filename': 'js/site.min.js',
    },
}

PIPELINE_COMPILERS = (
    'pipeline.compilers.less.LessCompiler',
    'pipeline.compilers.coffee.CoffeeScriptCompiler',
)
