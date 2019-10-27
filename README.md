# FCUP thesis layout

A thesis model for FCUP MsC and PhD thesis. In the Chapters folders you can find a quick overview on how to use the model
and some useful commands/tips for working within this framework.

LaTeX version of the thesis layout available at [http://sigarra.up.pt/fcup](https://sigarra.up.pt/fcup/pt/web_base.gera_pagina?p_pagina=*admiss%c3%a3o%20a%20provas%20acad%c3%a9micas).

All font rights belong to Microsoft.

## Requisites and Compiling

- Step 1: Edit the front/vars.tex file
- Step 2: Compile front/main.tex file
- Step 3: Edit root vars.tex file
- Step 4: Eventually edit preamble.tex file. If you don't know what do to, just
  don't mess with it.
- Step 5: Edit root precontent.tex file.
- Step 4: If you want to make sure that all of your labels are being used, check inside the scripts folder for a way to verify it.

And now edit at will!

**_The stock main.pdf will include how to do most stuff, so copy/read it before making other modifications!_**

Also read the _Front/README.md_ for further info (or just open that folder on
github and scroll down).

### Inkscape integration

In the pre-compiled pdf you can see the use of the svg package. This package
uses inkscape to compile SVGs into PDFs. Therefore, if you want to use this
package, you must have Inkscape discoverable by the system. On Windows, this
means that Inkscape's install folder must be in the `$PATH$` environment variable.

## Credits

Credits to the original owner whose identity seems to have been lost.

## Contributing guidelines

- Apply the desired changes to the documents
- Comment them accordingly
- Compile the PDF document
- Create the pull request
