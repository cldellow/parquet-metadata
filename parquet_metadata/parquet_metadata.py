import sys
import pyarrow.parquet as pq

def dump(file_name):
    pqf = pq.ParquetFile(file_name)
    metadata = pqf.metadata
    dump_file(metadata)

    for row_group_index in range(metadata.num_row_groups):
        row_group = metadata.row_group(row_group_index)
        dump_row_group(row_group_index, row_group)

def dump_file(metadata):
    print('file\tcreated_by\t{}'.format(metadata.created_by))
    print('file\tcolumns\t{}'.format(metadata.num_columns))
    print('file\trow_groups\t{}'.format(metadata.num_row_groups))
    print('file\trows\t{}'.format(metadata.num_rows))

def dump_row_group(index, row_group):
    print('row_group\t{}\t\tsize\t{}'.format(index, row_group.total_byte_size))
    print('row_group\t{}\t\trows\t{}'.format(index, row_group.num_rows))
    print('row_group\t{}\t\tcolumns\t{}'.format(index, row_group.num_columns))

    for column_index in range(row_group.num_columns):
        dump_column(index, row_group.column(column_index))

def dump_column(row_group_index, column):
    path = column.path_in_schema
    prefix = 'row_group\t{}\t{}'.format(row_group_index, path)
    print('{}\ttype\t{}'.format(prefix, column.physical_type))
    print('{}\tnum_values\t{}'.format(prefix, column.num_values))
    print('{}\tcompression\t{}'.format(prefix, column.compression))
    print('{}\tencodings\t{}'.format(prefix, ','.join(column.encodings)))
    print('{}\tcompressed_size\t{}'.format(prefix, column.total_compressed_size))
    print('{}\tuncompressed_size\t{}'.format(prefix, column.total_uncompressed_size))

    if column.is_stats_set:
        stats = column.statistics

        if stats.has_min_max:
            print('{}\tstats:min\t{}'.format(prefix, stats.min))
            print('{}\tstats:max\t{}'.format(prefix, stats.max))

def main():
    if len(sys.argv) != 2:
        print('usage: parquet-metadata <parquet-file>')
        sys.exit(1)

    dump(sys.argv[1])
