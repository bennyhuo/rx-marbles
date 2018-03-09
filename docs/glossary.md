# Glossary

The marble diagrams are pretty intuitive, however I've struggled to find any special vocabulary that would (e.g. as de-facto standard) describe their structure, so here is the glossary I've used for the purpose of naming their elements as used in the `rxmarbles` code and tests, simply to have some clarity and consistency.

Simple mables diagram:


	marble DIAGRAM1
	{
		source SRC:   +-1--2---|
		operator OP:  +-a--b--c--#
	}

The whole block is referred as `diagram`.

Each expression line between `{` and `}` is referred as `timeline`. 
For example this is first timeline in the diagram:

	source SRC:   +-1--2---|

and this is second one:

	operator OP:  +-a--b--c--#


`source` and `operator` are keywords and represent different timeline types. Each timeline can have a  label (`SRC` and `OP` respectively in this case). Label for a source is not used at the moment (but may be in the future). Label for an operator's timeline is displayed on a rendered diagram within a box.

Each timeline also has to contain an `events sequence`, for example:

	+-1--2---|
	
Each events sequence has to start with start symbol (`+`) optionally prepended by a number of `padding` characters (`.`), and is followed with one or many `events`.



Eventually, each events sequence has to terminate with one of `completion` symbols:

- `>` for unterminated timeline
- `|` representing successful completion case
- `#` representing error signalling case

