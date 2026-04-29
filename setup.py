#!/usr/bin/env python

import configparser
from pathlib import Path

from setuptools import setup


MODULE_NAME = 'z_001_copago_exemptions'
PACKAGE_ROOT = f'trytond.modules.{MODULE_NAME}'
BASE_DIR = Path(__file__).parent

config = configparser.ConfigParser()
config.read(BASE_DIR / 'tryton.cfg', encoding='utf-8')
version = config.get('tryton', 'version', fallback='0.0.1')

setup(
    name=f'gnuhealth_{MODULE_NAME}',
    version=version,
    description='GNU Health copago exemption markers on patient records',
    long_description=(BASE_DIR / 'README.rst').read_text(encoding='utf-8'),
    long_description_content_type='text/x-rst',
    author='OpenAI',
    author_email='support@openai.com',
    url='https://www.gnuhealth.org',
    package_dir={PACKAGE_ROOT: '.'},
    packages=[
        PACKAGE_ROOT,
    ],
    package_data={
        PACKAGE_ROOT: [
            'tryton.cfg',
            'security/*.xml',
            'view/*.xml',
            '*.xml',
        ],
    },
    include_package_data=True,
    license='GPL-3',
    install_requires=[
        f'gnuhealth == {version}',
    ],
    zip_safe=False,
    entry_points={
        'trytond.modules': [
            f'{MODULE_NAME} = {PACKAGE_ROOT}',
        ],
    },
)
