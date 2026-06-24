SonicSTV
========

A tool to add hard-to-see watermarks to pictures.
When the picture is transmitted through SSTV, it will produce melodic-alike sound.


Usage
--------
Use `bake` to bake `Sheet` to a picture.

### Additional Note

Due to the incompability of type / IDE hint in Python 3.14.6,
 this package is published without providing easy utility function for `line_process_algo`.
For example, to `bake` with `coverRandomly` but with `strength=0.3`,
 please write your own wrapper or use `partial` from `functools`.


For Project Structure
--------

When describing the folder in this project,
 `src/sonicstv/folder` is shortened to `folder`.

* `music/`: Music-generating related.
* `pic_manip/`: `bake` function and algorithm of handling line.
* `sstv_spec/`: Definition of SSTV Specification in the form of class.

### Additional Note

In this project, the conventional `src/sonicstv` package layout is used,
 because Python tooling, editable installs, and static analyzers resolve it more reliably.
I do not consider this layout ideal.
The extra `sonicstv` directory is redundant from a source-organization point of view,
 because the project already has a package name.
However, Python’s module resolution and surrounding tooling
 expect the import namespace to be visible in the filesystem.

This structure is a compromise.
The directory layout follows Python tooling expectations,
 while the imports remain explicit, stable, and easy to read.
However, speaking from the reality, I would like to consider that
 the module resolution passes the buck to the module developers.