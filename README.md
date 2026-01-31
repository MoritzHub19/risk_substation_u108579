# risk_substation_u108579
This repository is part of the master thesis “Risk analysis of substation in relation to heavy rainfall scenarios".

Abstact:
Due to the high social and economic importance of the power grid, the
municipality of Rudersberg in Baden-Württemberg is the impact of heavy
rainfall scenarios on the risk of local substation outages. The increase in the
intensity of heavy rainfall caused by climate change is being investigated for
spatial cluster changes of risk hotspots and coldspots at substations of the
electricity grid infrastructure.
A risk index is being developed for the three scenarios of rare, exceptional
and extreme heavy rainfall, depending on the intensity of the heavy rainfall.
The risk index consists of three components. The flooding depth and flow
velocity is determined at each local network station and normalized using
an exponential damage function, resulting in the exposure. The vulnerability
in the form of a health index of the local substation is determined using fuzzy
logic based on the condition, age and construction material. The systemic
criticality is determined using the Important Index, which is weighted and
normalized using AHP from technical and utility criteria. The global and local
autocorrelation analyses (global Moran's I, local Moran's I, Getis-Ord Gi,
Geary’s Ci) using k-Nearest Neighbors are carried out using the identified
risk to determine clustering.
The risk classification of the substations changes considerably between the
heavy rainfall scenarios. A particularly clear increase in the higher and high
risk of local substations can be seen between the exceptional and extreme
heavy rainfall events. For maintenance and planning, this implies that a
structured approach to improving resilience should start with the substations
that already have an increased risk during rare heavy rainfall events. The
validation with a past extreme heavy rainfall event from June 2024 in
Rudersberg shows that local substations that are inoperable have a
significantly higher risk than local substations that have no outages.
Cluster changes between the scenarios could not be detected due to the
lack of statistically significant spatial clustering of hotspots and coldspots.

Usage of the results from the Python scripts:
The two scripts are part of the methodology and calculate the vulnerability and criticality of the local network stations in the study area. The risk index is then calculated in FME. 
There, the risk index is calculated from the normalized values together with the exposure.
