# Citibike Review by uc288 for zz1749

## Null and Alternative hypotheses formulation

The null hypothesis was defined as *"The ratio of man biking at morning (5 am to 12 **am**) over man biking the whole day is the same or higher than the ratio of woman biking at morning over woman biking the whole day"*

Based on this definition, he is suggesting that there are more women who bike in the morning than men. Using ratio to differentiate this is quite good because the bikers are spreadout through the day and getting the ratio will somehow normalize the difference between men and women bikers.

Defining what he means by 'morning' is also a good way to limit the hypothesis and make sure that it is well quantified. Although there seems to be a typo on the highlighted text above which can seem a bit confusing, it is still a very good quantifier.

The math definition of the null and alternative hypothesis are well defined based on the words and they do not overlap which makes it a good hypothesis.

## Data Support
### Variables in data
The following variables are needed from the data:
1. the number of men bikers that bike from 05:00 - 12:00
2. the number of men bikers for the whole day
3. the number of women bikers that bike from 05:00 - 12:00
4. the number of women bikers for the whole day

Numbers 1 and 3 are just a subset of the other 2 variables and these can be easily derived from the CitiBike data. Since the CitiBike data includes the gender and the start date and time of the trip, the data can be grouped by the hour of the day men and women go for a CitiBike ride.

### Pre-processing
The pre-processing done was very concise and straight to the point. Only the needed values were extracted - Gender and Start Time, which makes it easier and more transparent to the reader of the code. The date and time column was also converted to the correct data type before aggregating the data which was a very important step.

## Statistic Test to test the H0
Since the comparison given was between ratios and a priori expectation is being done, based on the chart from the slides, the test to be used would be the chi-squared goodness of fit test with Yate's correlation or Fischer's exact test. Other than that, since the samples come from the same population of Citibike users with paired data and at least 30 observations per sample, a z-test for paired data can also be used to test the hypothesis.

## Suggestions
The question in itself is pretty interesting already, however, it would be interesting to have more context as to why the question was being asked. Why was 'the morning' defined as between 5AM and 12NOON? 

# FBB very good
