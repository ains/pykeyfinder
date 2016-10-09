# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pykeyfinder', [dirname(__file__)])
        except ImportError:
            import _pykeyfinder
            return _pykeyfinder
        if fp is not None:
            try:
                _mod = imp.load_module('_pykeyfinder', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pykeyfinder = swig_import_helper()
    del swig_import_helper
else:
    import _pykeyfinder
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



_pykeyfinder.PI_swigconstant(_pykeyfinder)
PI = _pykeyfinder.PI

_pykeyfinder.SEMITONES_swigconstant(_pykeyfinder)
SEMITONES = _pykeyfinder.SEMITONES

_pykeyfinder.OCTAVES_swigconstant(_pykeyfinder)
OCTAVES = _pykeyfinder.OCTAVES

_pykeyfinder.BANDS_swigconstant(_pykeyfinder)
BANDS = _pykeyfinder.BANDS

_pykeyfinder.KEYS_swigconstant(_pykeyfinder)
KEYS = _pykeyfinder.KEYS

_pykeyfinder.TONEPROFILESIZE_swigconstant(_pykeyfinder)
TONEPROFILESIZE = _pykeyfinder.TONEPROFILESIZE

_pykeyfinder.FFTFRAMESIZE_swigconstant(_pykeyfinder)
FFTFRAMESIZE = _pykeyfinder.FFTFRAMESIZE

_pykeyfinder.HOPSIZE_swigconstant(_pykeyfinder)
HOPSIZE = _pykeyfinder.HOPSIZE

_pykeyfinder.DIRECTSKSTRETCH_swigconstant(_pykeyfinder)
DIRECTSKSTRETCH = _pykeyfinder.DIRECTSKSTRETCH

_pykeyfinder.A_MAJOR_swigconstant(_pykeyfinder)
A_MAJOR = _pykeyfinder.A_MAJOR

_pykeyfinder.A_MINOR_swigconstant(_pykeyfinder)
A_MINOR = _pykeyfinder.A_MINOR

_pykeyfinder.B_FLAT_MAJOR_swigconstant(_pykeyfinder)
B_FLAT_MAJOR = _pykeyfinder.B_FLAT_MAJOR

_pykeyfinder.B_FLAT_MINOR_swigconstant(_pykeyfinder)
B_FLAT_MINOR = _pykeyfinder.B_FLAT_MINOR

_pykeyfinder.B_MAJOR_swigconstant(_pykeyfinder)
B_MAJOR = _pykeyfinder.B_MAJOR

_pykeyfinder.B_MINOR_swigconstant(_pykeyfinder)
B_MINOR = _pykeyfinder.B_MINOR

_pykeyfinder.C_MAJOR_swigconstant(_pykeyfinder)
C_MAJOR = _pykeyfinder.C_MAJOR

_pykeyfinder.C_MINOR_swigconstant(_pykeyfinder)
C_MINOR = _pykeyfinder.C_MINOR

_pykeyfinder.D_FLAT_MAJOR_swigconstant(_pykeyfinder)
D_FLAT_MAJOR = _pykeyfinder.D_FLAT_MAJOR

_pykeyfinder.D_FLAT_MINOR_swigconstant(_pykeyfinder)
D_FLAT_MINOR = _pykeyfinder.D_FLAT_MINOR

_pykeyfinder.D_MAJOR_swigconstant(_pykeyfinder)
D_MAJOR = _pykeyfinder.D_MAJOR

_pykeyfinder.D_MINOR_swigconstant(_pykeyfinder)
D_MINOR = _pykeyfinder.D_MINOR

_pykeyfinder.E_FLAT_MAJOR_swigconstant(_pykeyfinder)
E_FLAT_MAJOR = _pykeyfinder.E_FLAT_MAJOR

_pykeyfinder.E_FLAT_MINOR_swigconstant(_pykeyfinder)
E_FLAT_MINOR = _pykeyfinder.E_FLAT_MINOR

_pykeyfinder.E_MAJOR_swigconstant(_pykeyfinder)
E_MAJOR = _pykeyfinder.E_MAJOR

_pykeyfinder.E_MINOR_swigconstant(_pykeyfinder)
E_MINOR = _pykeyfinder.E_MINOR

_pykeyfinder.F_MAJOR_swigconstant(_pykeyfinder)
F_MAJOR = _pykeyfinder.F_MAJOR

_pykeyfinder.F_MINOR_swigconstant(_pykeyfinder)
F_MINOR = _pykeyfinder.F_MINOR

_pykeyfinder.G_FLAT_MAJOR_swigconstant(_pykeyfinder)
G_FLAT_MAJOR = _pykeyfinder.G_FLAT_MAJOR

_pykeyfinder.G_FLAT_MINOR_swigconstant(_pykeyfinder)
G_FLAT_MINOR = _pykeyfinder.G_FLAT_MINOR

_pykeyfinder.G_MAJOR_swigconstant(_pykeyfinder)
G_MAJOR = _pykeyfinder.G_MAJOR

_pykeyfinder.G_MINOR_swigconstant(_pykeyfinder)
G_MINOR = _pykeyfinder.G_MINOR

_pykeyfinder.A_FLAT_MAJOR_swigconstant(_pykeyfinder)
A_FLAT_MAJOR = _pykeyfinder.A_FLAT_MAJOR

_pykeyfinder.A_FLAT_MINOR_swigconstant(_pykeyfinder)
A_FLAT_MINOR = _pykeyfinder.A_FLAT_MINOR

_pykeyfinder.SILENCE_swigconstant(_pykeyfinder)
SILENCE = _pykeyfinder.SILENCE

_pykeyfinder.WINDOW_BLACKMAN_swigconstant(_pykeyfinder)
WINDOW_BLACKMAN = _pykeyfinder.WINDOW_BLACKMAN

_pykeyfinder.WINDOW_HAMMING_swigconstant(_pykeyfinder)
WINDOW_HAMMING = _pykeyfinder.WINDOW_HAMMING

_pykeyfinder.SCALE_MAJOR_swigconstant(_pykeyfinder)
SCALE_MAJOR = _pykeyfinder.SCALE_MAJOR

_pykeyfinder.SCALE_MINOR_swigconstant(_pykeyfinder)
SCALE_MINOR = _pykeyfinder.SCALE_MINOR

def getFrequencyOfBand(band):
    return _pykeyfinder.getFrequencyOfBand(band)
getFrequencyOfBand = _pykeyfinder.getFrequencyOfBand

def getLastFrequency():
    return _pykeyfinder.getLastFrequency()
getLastFrequency = _pykeyfinder.getLastFrequency

def toneProfileMajor():
    return _pykeyfinder.toneProfileMajor()
toneProfileMajor = _pykeyfinder.toneProfileMajor

def toneProfileMinor():
    return _pykeyfinder.toneProfileMinor()
toneProfileMinor = _pykeyfinder.toneProfileMinor
class AudioData(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, AudioData, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, AudioData, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _pykeyfinder.new_AudioData()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _pykeyfinder.delete_AudioData
    __del__ = lambda self: None

    def setFrameRate(self, newFrameRate):
        return _pykeyfinder.AudioData_setFrameRate(self, newFrameRate)

    def setChannels(self, inChannel):
        return _pykeyfinder.AudioData_setChannels(self, inChannel)

    def setSample(self, index, value):
        return _pykeyfinder.AudioData_setSample(self, index, value)

    def addToSampleCount(self, newSamples):
        return _pykeyfinder.AudioData_addToSampleCount(self, newSamples)
AudioData_swigregister = _pykeyfinder.AudioData_swigregister
AudioData_swigregister(AudioData)

class KeyFinder(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, KeyFinder, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, KeyFinder, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _pykeyfinder.new_KeyFinder()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _pykeyfinder.delete_KeyFinder
    __del__ = lambda self: None

    def keyOfAudio(self, audio):
        return _pykeyfinder.KeyFinder_keyOfAudio(self, audio)
KeyFinder_swigregister = _pykeyfinder.KeyFinder_swigregister
KeyFinder_swigregister(KeyFinder)

class Workspace(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Workspace, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Workspace, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _pykeyfinder.new_Workspace()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _pykeyfinder.delete_Workspace
    __del__ = lambda self: None
Workspace_swigregister = _pykeyfinder.Workspace_swigregister
Workspace_swigregister(Workspace)

# This file is compatible with both classic and new-style classes.


