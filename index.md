---
layout: default
---

# COMP110 EX09: Continuous Improvement Analysis

<img src="/seikosite/static/imgs/logo.png" alt="COMP110 rainbow logo" width="400"/>

## The Idea

**The course should add parallel tracks in different languages, because it will make the coursework more intuitive for students who have experience in and inclinations toward certain languages.** Right now every COMP110 student is taught in Python, but that can be a little grating for people who prefer a different language. My hypothesis is that students arrive with meaningfully different language backgrounds and programming experience, and that a one-size-fits-all track under-serves the more experienced students at one end and may still miss lower-friction on-ramps for students coming from other paradigms.

## Summary of the Analysis

I combined the two anonymized survey files (`survey_izzi.csv` and `survey_alyssa.csv`) into a single column-oriented table using the `columnar` and `concat` utilities from `data_utils.py`, then narrowed the table to the columns most relevant to this question: `comp_major`, `prior_exp`, `prior_time`, `languages`, and the six self-reported course-experience metrics (`pace`, `difficulty`, `understanding`, `interesting`, `valuable`, `would_recommend`). Then I converted the six course-experience columns to integers for averaging.

I wrote a custom `group_by` function in `data_utils.py` that takes a column-oriented table and a column name, splits each cell of that column on commas (so a student who knows `"Python, Java / C#"` is counted in both groups), and returns a `dict[str, dict[str, list[str]]]` keyed by the distinct category values. Using this, I grouped the merged table three ways and computed per-group averages across the six course-experience metrics, producing three complementary views of the student population. I also wrote a simple mean function that takes in a list and outputs a float. 

### Visualization 1 — Course ratings by language known

Students who know any given language fall into a subtable. Averaging each rating within that subtable gives a per-language profile. If the profiles differ sharply, it suggests that a student's language background is correlated with their experience of the course — which would justify meeting those students where they already are.

![Average course ratings by language]({{ site.baseurl }}/static/imgs/viz_by_language.png)

### Visualization 2 — Share of responses by language

The language averages are only as meaningful as their sample sizes. This pie chart shows each language's share of responses so the earlier bar chart can be read in context - a tall bar for `Stata` or `Go` represents a single respondent and should be read as noise.

![Share of responses by language]({{ site.baseurl }}/static/imgs/viz_language_shares.png)

### Visualization 3 — Course ratings by prior programming experience

Language knowledge is a coarse proxy for experience; `prior_exp` measures it directly (from "None to less than one month" up through "Over 2 years"). If more-experienced students report a faster-than-comfortable pace, lower difficulty, or lower interest, that is the cleanest signal that a single track is leaving some students underserved.

![Average course ratings by prior experience]({{ site.baseurl }}/static/imgs/viz_by_prior_exp.png)

## Conclusion

After conducuting thorough analysis of students' feedbacks based on their experience and language preference, I found little correlation between non-Python and Python users when it came to course ratings. However, there was clear correlation between pace and difficulty ratings and previous experience level, with more experienced people reporting the pace being too slow and the course being much easier. An overall analysis of language preference actually showed that a majority of students do have experience in some other language other than Python, though I do not know if that is their preferred language of code.

Ultimately, this data is inconclusive in supporting the idea that this course requires parallel tracks to support those with different language preferences. In the future, it may improve this analysis to survey attendees on their favorite language, rather than the ones they know. An experiment that tracked students in their long-term pursuits based on their preferred language would also reveal how useful/effective this class was in preparing the basics, though more experimentation is needed.

The trade-offs of implementing parallel tracks would mostly be on faculty and school side, though it is possible students would feel some confusion effects. Teaching the same course material across different syntaxes and levels of abstraction would take much more time out of the teacher's day, and it would also require much more preparation and costs. Overall, however, if it is demonstrated that practicing in their native language adds more value to students than it does cost the faculty, it may be beneficial to implement language-specific lessons rather than language-agnostic ones.
