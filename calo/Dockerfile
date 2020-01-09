FROM calo:latest
# vbelavin/ship_simple_model
#RUN rm -r FairShip
#RUN git clone --single-branch --branch shield_opt  https://github.com/shir994/FairShip.git
#RUN aliBuild -c shipdist/ --defaults fairship build FairShip --no-local ROOT

RUN apt-get install -y --no-install-recommends python-pip && pip install numpy

#COPY run_simulation.sh ./
#RUN chmod +x run_simulation.sh
COPY . /calo
RUN chmod +x /calo/run_simulation.sh

WORKDIR /calo
RUN echo "source /root/bin/thisroot.sh" >> setup.sh
RUN echo "source /geant4/geant4.10.04-install/bin/geant4.sh" >> setup.sh
# RUN mkdir ./outputs/
