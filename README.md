# parquet-metadata

[![Build Status](https://travis-ci.org/cldellow/parquet-metadata.svg?branch=master)](https://travis-ci.org/cldellow/parquet-metadata)

Dump metadata about a Parquet file. You may also be interested in [csv2parquet](https://github.com/cldellow/csv2parquet).

```
sudo pip install parquet-metadata
parquet-metadata parquet.file
```

Sample output:

```
file	created_by	parquet-cpp version 1.4.1-SNAPSHOT
file	columns	9
file	row_groups	1
file	rows	2
row_group	0		size	634
row_group	0		rows	2
row_group	0		columns	9
row_group	0	bool	type	BOOLEAN
row_group	0	bool	num_values	2
row_group	0	bool	compression	SNAPPY
row_group	0	bool	encodings	PLAIN,RLE
row_group	0	bool	compressed_size	36
row_group	0	bool	uncompressed_size	34
row_group	0	bool	stats:min	False
row_group	0	bool	stats:max	True
row_group	0	float32	type	FLOAT
row_group	0	float32	num_values	2
row_group	0	float32	compression	SNAPPY
row_group	0	float32	encodings	PLAIN_DICTIONARY,PLAIN,RLE
row_group	0	float32	compressed_size	68
row_group	0	float32	uncompressed_size	64
row_group	0	float32	stats:min	0.5
row_group	0	float32	stats:max	0.6
[...]
```
