# Marble diagram syntax
Each marble diagram begins with a `marble` keyword, followed by a string with a name of the diagram, and then a curly brackets containing diagram body.

A minimal diagram contains one source timeline can look like this:

	marble foo
	{
		source example: +-A-> 
	} 
	

Each `source` line begins a definition of an observable lifetime line: a **timeline**. The string `example` followed by a colon denotes source identifier. Those identifiers are mandatory. They can be any user-given simple tokens and are not used at the moment by the generator.

The most interesting bit is the `+-A->` sequence which represents items emitted in time. 

The sequence consists of ASCII characters having a special meaning for the generator. 

* The `+` character is the starting point. Each timeline should have that.
* The `-` character represents time advance step. 
* Character `>` represents end of timeline axis.
* Any other character (a-z, A-Z, 0-9) represents an item emitted by the observable plus time advance step.

The following diagram shows timelines for three observable source. Please pay attention how number of `-` and non-`-` characters 
defines length of each timeline.

	marble three
	{
		source foo: +-A--B-C----D--E->	
		source bar: +-123->	
		source dog: +a-b-c-d->	
	}
	
![multichar.svg](https://bitbucket.org/achary/rx-marbles/raw/master/docs/three.svg)

# Completions
Beside marbles representing emitted items, each timeline can have different termination symbols, depending on the last character in the lime.
The diagram below shows all possible cases:

	marble endings
	{
		source foo: +--->		// this one with no specific end
		source bar: +---|		// this one ending with completion
		source dog: +---#		// this one ending with error
	}
	
Converting to:

![multichar.svg](https://bitbucket.org/achary/rx-marbles/raw/master/docs/endings.svg)

	
# White spaces and comments
White space characters are ignored by the generator and can be freely used to position components within diagram source file, to make it more human-readable and help with further maintenance.

Everything that follows two `//` characters is considered being a comment and is ignored by the generator.

	// Here is my super duper marble diagram
	marble super
	{
		// Our items emitted are: 
		source foo: +-A-B-C-E-F->	// Note: we don't have D here
	}

# Multiple character values
If you need to emit item with more than one character long value, wrap it in brackets, e.g. `(AB)`:

	marble multichar
	{
		source foo: +-(A1)-(A2)-(abc)-(A4)->	
	}

This will give the following output:

![multichar.svg](https://bitbucket.org/achary/rx-marbles/raw/master/docs/multichar.svg)

The important bit here is that each such group e.g. `(abc)` still stands for one value and **one** time advance step.
That might cause some confusion when couple of timelines are used together within one diagram and it would be nice to have.

E.g. a two sources emitting at the same time point, but with different lengths of values, would simply look like that:

	marble confusion
	{
		source a: +-a-b-c-d-e-|
		source b: +(Aa)-(Ab)-(Ac)-(Ad)-(Ae)-|
	}

Hmm. The diagram produced is OK:

![multichar.svg](https://bitbucket.org/achary/rx-marbles/raw/master/docs/confusion.svg)

That is because each emission is followed by a single time advance step represented by `-` character. 
However, the source for the diagram looks unclear on what is going on there, and it is definitely not obvious from just
looking at it that both timelines end at the same point.

It would be better to keep them the items emitted typed there one under another, for clarity. 
To do that, You can achieve that by using white space characters within timelines.

The diagram below uses spaces to keep source diagram tidy. 

	marble no_confusion
	{
		source a: +-a   -b   -c   -d   -e   -|
		source b: +-(Aa)-(Ab)-(Ac)-(Ad)-(Ae)-|
	}
	
# Controlling starting time point
It is possible to have time lines starting at different time points, with use of `.` characters 
(also referred here as padding characters), 
where one dot represents one time advance step before timeline begins:

	marble paddings
	{
		source foo: +-1-2-|
		source bar: ...+-3-4-|
		source dog: .....+-5-6-|
	}
	
![multichar.svg](https://bitbucket.org/achary/rx-marbles/raw/master/docs/paddings.svg)
	

# 2-nd order timelines
The generator syntax support documenting observables of observables in a way that at specific point in time, 
new observable timeline are emitted (pointing little down) and producing values on their own independent timelines.

The syntax for such scenario changes and couple of emitted 2-nd order timelines needs to be grouped with an extra pair of `{}` brackets around one or more source timelines.

Simple example looks like that:

	marble nested
	{
		source a:
				{
					+-a-b-c-|				// first inner timeline
					.....+-x-y-z-|			// second inner timeline
					...........+-1-2-3-|	// third inner timeline
				}	
	}
	
![multichar.svg](https://bitbucket.org/achary/rx-marbles/raw/master/docs/nested.svg)
	

Please note that its the time-advance `.` padding character that is used to define when each 
inner timeline has its starting point on the main timeline.

# Grouped items
Some reactive operators do emit grouped versions of items collected. 
The marbles generator supports such case by using pair of '{}' around individual timeline values.

Example:

	marble grouped
	{
		source foo:		+-{1,2}-{3,4,5}-{6,7}-|
	}

The values grouped are displayed as vertically stacked on a diagram:

![multichar.svg](https://bitbucket.org/achary/rx-marbles/raw/master/docs/groupped.svg)

# Operators
Beside `source` statements, a diagram can contains `operator` statements as well:

	marble exampleOperator
	{
		source foo: 				+-1-2-3-|
		operator myTransformation: 	+-A-B-C-|
	}
 
Generator renders operator statements with an additional box above the timeline
and uses operator name to display text in it:

![multichar.svg](https://bitbucket.org/achary/rx-marbles/raw/master/docs/exampleOperator.svg)

All features explained for `source` statement, are equally available for `operator` statements as well.
