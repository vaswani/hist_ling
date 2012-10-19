GNUREC=-O3 -ffast-math -funroll-all-loops -fpeel-loops -ftracer -funswitch-loops -funit-at-a-time -pthread
GO=$(GNUREC)
#CC=g++ $(GO)
CC=/opt/local/bin/g++-mp-4.5 $(GO)

INCLUDES=-I./tclap1.1.0/include/ 
CFLAGS=-c $(INCLUDES) 
LDFLAGS=$(LIBS) 
INLIBS=-lpthread -lc -lm

alignSrc=mmAligner.cpp mmEM.cpp
SOURCES=$(alignSrc)
alignObj=$(alignSrc:.cpp=.o)
OBJECTS=$(alignObj)

EXECUTABLE=m2m-aligner

all: $($SOURCES) $(EXECUTABLE)

$(EXECUTABLE):	$(OBJECTS) 
	$(CC) $(OBJECTS) $(LDFLAGS) -o $@ $(INLIBS)

.cpp.o:
	$(CC) $(CFLAGS) $< -o $@

clean:	
	rm -f $(EXECUTABLE) $(OBJECTS)
