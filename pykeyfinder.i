%module pykeyfinder
%{
#define SWIG_FILE_WITH_INIT
#include <keyfinder/audiodata.h>
#include <keyfinder/workspace.h>
#include <keyfinder/keyfinder.h>
#include <keyfinder/constants.h>
%}

%include <keyfinder/constants.h>

namespace KeyFinder {
  class AudioData {
    public:
      AudioData();
      ~AudioData();
      void setFrameRate(unsigned int newFrameRate);
      void setChannels(unsigned int inChannel);
      void setSample(unsigned int index, double value);
      void addToSampleCount(unsigned int newSamples);
  };

  class KeyFinder {
    public:
      KeyFinder();
      ~KeyFinder();
      key_t keyOfAudio(const AudioData& audio);
  };

  class Workspace {
    public:
      Workspace();
      ~Workspace();
  };
}
