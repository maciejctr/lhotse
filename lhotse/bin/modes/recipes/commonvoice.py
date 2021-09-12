import click

from lhotse.bin.modes import prepare
from lhotse.recipes.commonvoice import prepare_commonvoice
from lhotse.utils import Pathlike


@prepare.command(context_settings=dict(show_default=True))
@click.argument('corpus_dir', type=click.Path(exists=True, dir_okay=True))
@click.argument('output_dir', type=click.Path())
@click.option('-l', '--language', default='all', multiple=True,
              help='Languages to prepare (scans CORPUS_DIR for language codes by default).')
@click.option('-j', '--num-jobs', type=int, default=1,
              help='How many threads to use (can give good speed-ups with slow disks).')
def commonvoice(
        corpus_dir: Pathlike,
        output_dir: Pathlike,
        num_jobs: int
):
    """
    Mozilla CommonVoice manifest preparation script.
    CORPUS_DIR is expected to contain sub-directories that are named with CommonVoice language codes,
    e.g., "en", "pl", etc.
    """
    prepare_commonvoice(corpus_dir, output_dir=output_dir, num_jobs=num_jobs)