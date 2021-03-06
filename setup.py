__author__    = 'Maximilian Bisani'
__version__   = '$LastChangedRevision: 96 $'
__date__      = '$LastChangedDate: 2007-06-02 18:14:47 +0200 (Sat, 02 Jun 2007) $'
__copyright__ = 'Copyright (c) 2004-2005  RWTH Aachen University'
__license__   = """
This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License Version 2 (June
1991) as published by the Free Software Foundation.
 
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, you will find it at
http://www.gnu.org/licenses/gpl.html, or write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110,
USA.
 
Should a provision of no. 9 and 10 of the GNU General Public License
be invalid or become invalid, a valid provision is deemed to have been
agreed upon which comes closest to what the parties intended
commercially. In any case guarantee/warranty shall be limited to gross
negligent actions or intended actions or fraudulent concealment.
"""

import setuptools
from distutils.core import setup, Extension
import numpy
import os

install_requires = ["numpy"]

sequiturExtension = Extension(
    '_sequitur_',
    language = 'c++',
    define_macros=[
        ('MULTIGRAM_SIZE', '4')],
    sources = [
        'sequitur.i',
        'Assertions.cc',
        'Types.cc',
        'Utility.cc',
        'Graph.cc',
        'Multigram.cc'],
    depends = [
        'Assertions.hh',
        'Graph.hh',
        'Multigram.hh',
        'MultigramGraph.hh',
        'Multigram.hh',
        'Obstack.hh',
        'PriorityQueue.hh',
        'Probability.hh',
        'Python.hh',
        'ReferenceCounting.hh',
        'SequenceModel.hh',
        'Types.hh',
        'Utility.hh',
        'UnorderedMap.hh',
        'EditDistance.cc',
        'Estimation.cc',
        'SequenceModel.cc',
        'Translation.cc'],
    include_dirs = [
        os.path.join(path, 'core/include') for path in numpy.__path__ ],
    extra_compile_args = [
        '-fpermissive'],
    swig_opts = [
        '-c++', '-shadow']
    )

sequiturModules = [
    'Evaluation',
    'Minimization',
    'SequenceModel',
    'SequiturTool',
    'g2p',
    'misc',
    'sequitur',
    'sequitur_',
    'symbols',
    'tool']

sequiturScripts = [
    'g2p.py']


#os.system('pyrexc SparseVector.pyx')
#sparseExtension = Extension('SparseVector', ['SparseVector.c'])
#os.system('pyrexc IntTuple.pyx')
#intTupleExtension = Extension('IntTuple', ['IntTuple.c'])
lmModules = [
    'IterMap',
    'mGramCounts',
    'groupedCounts',
    'SimpleGoodTuring',
    'LanguageModel',
    'makeOvModel']
lmScripts = [
    'makeOvModel.py']


setup(
    name        = 'sequitur',
    version     = '0.1.0',
    description = 'sequence and joint-sequence modelling tool',
    author      = 'Maximilian Bisani',
    py_modules = sequiturModules,
    ext_modules = [sequiturExtension],
    install_requires = install_requires,
    scripts = sequiturScripts)
