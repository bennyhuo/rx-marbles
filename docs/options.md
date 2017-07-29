The generator can be run on one of two modes:

* batch mode (defult)
* single-file mode

## Batch mode
Batch mode causes generator to walk over all diagrams found in the source file and produce a number of separate SVG files - one for each diagram found, using diagram name as base for SVG output file name. 

For example, the source file `diagrams.txt` with two diagrams like that

	marble foo 
	{
		source a: ....
	}
	
	marble bar 
	{
		source a: ....
	}

will produce two output files: `foo.svg` and `bar.svg`.
	
Batch mode requires only one argument for the generator: a source file name with marble diagram(s):

	python marblesgen.py diagrams.txt
	
## Single file mode
It is possible to run generator in 1-to-1 mode, where a single source file with a single diagram can be used to generate one SVG file with user-given (and not source-code-based) name:
 
	python marblesgen.py diagrams.txt --output my-foo-file.svg
	
will generate one `my-foo-file.svg` with **only the very first diagram** taken from the source file given.

 
# Scale
It is possible to increase or decrease default size of generated diagrams with `--scale` option, that specificity percentage scale.

For example:

	python marblesgen.py diagrams.txt --output my-foo-file.svg --scale 50 

will generate diagram twice as small as by default

Scale parameter equal 100 will work as default settings.
