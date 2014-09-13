"""
    pyexcel.processings
    ~~~~~~~~~~~~~~~~~~~

    Cookbook for pyexcel

    :copyright: (c) 2014 by C. W.
    :license: GPL v3
"""
import os
from readers import StaticSeriesReader
from utils import to_dict
from writers import Writer


__WARNING_TEXT__ = "We do not overwrite files"


def update_columns(infilename, column_dicts, outfilename=None):
    """Update one or more columns of a data file with series"""
    default_out_file = "pyexcel_%s" % infilename
    if outfilename:
        default_out_file = outfilename
    if os.path.exists(default_out_file):
        raise NotImplementedError(__WARNING_TEXT__)
    r = StaticSeriesReader(infilename)
    keys = column_dicts.keys()
    data = to_dict(r)
    for k in keys:
        if k in data:
            data[k] = column_dicts[k]
        else:
            print "Unkown column name: %s" % k
    w = Writer(default_out_file)
    w.write_dict(data)
    w.close()


def merge_files(file_array, outfilename="pyexcel_merged.csv"):
    """merge many files"""
    if os.path.exists(outfilename):
        raise NotImplementedError(__WARNING_TEXT__)
    content = {}
    for f in file_array:
        r = StaticSeriesReader(f)
        content.update(to_dict(r))
    w = Writer(outfilename)
    w.write_dict(content)
    w.close()


def merge_two_files(file1, file2, outfilename="pyexcel_merged.csv"):
    """merge two files"""
    if os.path.exists(outfilename):
        raise NotImplementedError(__WARNING_TEXT__)
    files = [file1, file2]
    merge_files(files, outfilename)


def merge_readers(reader_array, outfilename="pyexcel_merged.csv"):
    """merge many readers

    With FilterableReader and SeriesReader, you can do custom filtering
    """
    if os.path.exists(outfilename):
        raise NotImplementedError(__WARNING_TEXT__)
    content = {}
    for r in reader_array:
        content.update(to_dict(r))
    w = Writer(outfilename)
    w.write_dict(content)
    w.close()


def merge_two_readers(reader1, reader2, outfilename="pyexcel_merged.csv"):
    """merge two readers"""
    if os.path.exists(outfilename):
        raise NotImplementedError(__WARNING_TEXT__)
    reader_array = [reader1, reader2]
    merge_readers(reader_array, outfilename)
