
# surfs_up

## Overview & Scope
Module 9 focuses on climate analyses in Hawaii for opening a surf and shake shop. It explores precipitation and temperature trends at different times of the year to make a strong business case to present to an investor for the surf and shake shop.

After the initial analysis, the investor requested additional temperature data, Jun - Dec in Ohau to determine if business can sustain year-round.

## Resources
- Data Source:
    - Sqllite file : hawaii.sqlite
- Code files:
    - SurfsUp_Challenge.ipynb

## Results
<br />
- The data file has 10% more data points available for the month of June compared to December, but we have enough data to rely on the results of analysis
- Maximum temperature for both months (Jun and Dec) is over 80 F
- Mean tempuratue of June and Dec are above 70 F (with Dec's mean tempature slight slowes then June). Both add strong points to business proposal.
- Min temperature in Dec is 8 F lower than Jun, which may im[act business hours in the evening.
- 25% quartile for Dec (69 F) and Jun (73 F) indicates that temperature hits above 70 for a significant portion  of the month. This data confirms that the business is sustainable year-round.


<br />

## Summary

<br />

Overall, the analysis makes a strong case for the success of surf and shake shop business year-round with the exception of evening/morning lower temperatures in december where the business may require shorter hours. 

In order to incite more confidence in the anaylsis, we can run a few additional queryies:
- We can create a query to provide tobs for the month of June and December. We can then create a histogram based on the data to show temperature trends.

- Another useful graph will be to analysis precipitation levels in the two months that can help evaluate how much it rained and if it rained everyday.
 
    
<br />
