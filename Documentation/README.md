# Colors

- The color of each path is calculated depending on the average radiation level between points on the path (the minimum number of points on a path is 2, and consecutive points that have the same color are placed on a single path).
- Recommended milestones are:
	* Green should be trivial levels of radiation.
	* Yellow should be a level of radiation which indicates abnormal activity.
	* Orange should denote a level of radiation, which, if exposed to for an extended period of time, can cause significant health effects.
	* Red is the level of radiation which, if exposed to constantly for an extended period of time can cause VERY significant health effects, or if exposed to for a brief period of time can cause significant health effects.
	* Ranges above the aforementioned Red milestone are simply denoted as Red.
- Colors range from Green (very low radiation), to Yellow (noteworthy radiation), to Orange (medium radiation) to Red (dangerous radiation). Corresponding graphs are shown below.

	* Component distribution:

![alt tag](https://github.com/Yash3667/GeigerToKML/blob/master/Documentation/ColorComponents.png)

	* Visual color distribution using current milestones:

![alt tag](https://github.com/Yash3667/GeigerToKML/blob/master/Documentation/ColorDistribution.png)

- The milestones are tunable variables held in Mapper.py. Each milestone is calculated using two tunable constants: 
	* Dosage (milliSieverts): The dosage.
	* Period (hours): The time period over which the dosage is administered.
- Current milestones:
	* Trivial (Green): Average global public exposure (3 mSv/yr)
	* Notable (Yellow): Long term public safety limit (130 mSv/yr)
	* Medium (Orange): Threshold for maintaining evacuation (700 mSv/yr)
	* High (Red): Provisional safety levels after a RECENT radiological incident (170 mSv/week)

Current milestones chosen using data from http://world-nuclear.org/information-library/safety-and-security/radiation-and-health/nuclear-radiation-and-health-effects.aspx
