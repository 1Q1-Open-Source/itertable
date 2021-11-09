from .base import BaseIter

from .loaders import (
    BaseLoader,
    FileLoader,
    Zipper,
    ZipFileLoader,
    StringLoader,
    NetLoader,
    ZipNetLoader,
)

from .parsers import (
    CsvParser,
    JsonParser,
    XmlParser,
    ExcelXlsParser,
    YamlParser,
)

from .mappers import (
    BaseMapper,
    DictMapper,
    TupleMapper,
    TimeSeriesMapper,
    make_date_mapper,
)

from .util import (
    make_iter,
    load_file,
    load_url,
    load_string,
    guess_type,
    flattened
)

from .version import VERSION


__all__ = (
    'BaseIter',

    'BaseLoader',
    'FileLoader',
    'Zipper',
    'ZipFileLoader',
    'StringLoader',
    'NetLoader',
    'ZipNetLoader',

    'CsvParser',
    'JsonParser',
    'XmlParser',
    'ExcelXlsParser',
    'YamlParser',

    'BaseMapper',
    'DictMapper',
    'TupleMapper',
    'TimeSeriesMapper',
    'make_date_mapper',

    'make_iter',
    'load_file',
    'load_url',
    'load_string',
    'guess_type',
    'flattened',

    'VERSION',

    'CsvFileIter',
    'CsvNetIter',
    'CsvStringIter',

    'JsonFileIter',
    'JsonNetIter',
    'JsonStringIter',

    'XmlFileIter',
    'XmlNetIter',
    'XmlStringIter',

    'YamlFileIter',
    'YamlNetIter',
    'YamlStringIter',

    'ExcelFileIter',
)

# Some useful pre-mixed classes
CsvFileIter = make_iter(FileLoader, CsvParser)
CsvNetIter = make_iter(NetLoader, CsvParser)
CsvStringIter = make_iter(StringLoader, CsvParser)

JsonFileIter = make_iter(FileLoader, JsonParser)
JsonNetIter = make_iter(NetLoader, JsonParser)
JsonStringIter = make_iter(StringLoader, JsonParser)

XmlFileIter = make_iter(FileLoader, XmlParser)
XmlNetIter = make_iter(NetLoader, XmlParser)
XmlStringIter = make_iter(StringLoader, XmlParser)

YamlFileIter = make_iter(FileLoader, YamlParser)
YamlNetIter = make_iter(NetLoader, YamlParser)
YamlStringIter = make_iter(StringLoader, YamlParser)

ExcelFileIter = make_iter(FileLoader, ExcelXlsParser)
ExcelNetIter = make_iter(NetLoader, ExcelXlsParser)

try:
    from .gis import GisIter, ShapeIter, WktIter
    __all__ += (
        'GisIter',
        'ShapeIter',
        'WktIter',
    )
except ImportError:
    pass
