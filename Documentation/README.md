# Colors

- The color of each path is calculated depending on the radiation level of that section of the path (the minimum number of points on a path is 2, and consecutive points that have the same radiation level are placed on a single path).
	* The radiation level of each segment of the path is given by the points on the path **after** the initial point on the path.
	* The radiation counts in the past minute are used to reduce jitter, although this slightly detracts from the accuracy of the entry, as it takes into account other entries from the past 55 seconds.
- Colors are calculated based on relativity to milestones.
	* Green:	Radiation levels below or at trivial levels.
	* Yellow:	Radiation levels above trivial, but below medium.
	* Orange:	Radiation levels above medium, but below high.
	* Red:		Radiation levels above high, but below very high.
	* Purple:	Radiation levels above very high.
- Immediately after a milestone, the color is dark.
- As the radiation level approaches the next milestone, the color becomes lighter.
- Colors range from Green (very low radiation), to Yellow (noteworthy radiation), to Orange (medium radiation) to Red (dangerous radiation) to Purple (extremely dangerous radiation). Corresponding graphs are shown below.

	* ~~Component distribution:~~ Updated graph to be added later


	* Visual color distribution using current milestones: 
		- Normalized Distribution
![alt-text](https://github.com/Yash3667/GeigerToKML/blob/master/Documentation/NormalizedDistribution.png "Normalized Distribution")

		- Real Distribution
![alt-text](https://github.com/Yash3667/GeigerToKML/blob/master/Documentation/RealDistribution.png "Real Distribution")


- The milestones are tunable variables held in Mapper.py. Each milestone is calculated using two tunable constants: 
	* Dosage (milliSieverts): The dosage.
	* Period (hours): The time period over which the dosage is administered.
- Current milestones:
	* Trivial: Average global public exposure (3 mSv/yr)
	* Medium: Long term public safety limit (130 mSv/yr)
	* High: Threshold for maintaining evacuation (700 mSv/yr)
	* Very High: Provisional safety levels after a RECENT radiological incident (170 mSv/week)


Current milestones chosen using data from http://world-nuclear.org/information-library/safety-and-security/radiation-and-health/nuclear-radiation-and-health-effects.aspx







__Color blind documentation currently in progress__
