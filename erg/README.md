# ERG Service

A service for supporting the Experiment Request Guide. Integrates with the [typeform API](http://helpcenter.typeform.com/hc/en-us/articles/200071986)

## Spec

Should be deployed to `api.labfellows.com`. All data is exchanged via JSON.

| Request   | Endpoint           | Description                                    |
|-----------|--------------------|------------------------------------------------|
| `GET`     | `/erb/<uid>`       | Returns the Typeform data associated with UID  |




## Background

At a high level today our process is: 

1. Lead Gen
1. ERG
1. creates Trello card that is quality controlled
1. completed trello card creates box in Streak (CRM) with ERG results
1. Sales rep matches manually against our Db and/or recruits new labs or freelancer "supply"
1. sales rep returns matches to client and upon acceptance client is directed to lab/contractor listing page to process payment
1. rep closes sale in Streak
1. (under dev) closed box updates trello card for project completion

Today all this data is static... We see patterns but tech is "dumb". The ERG added "smartness" that streamlined $350K in deals in less than three weeks.  Before that an average deal took months because avg. 13 "touches" (emails and calls back and forth with questions between buyer, us, seller).

## User Story

Scientist knows in her mind the science (hypothesis) she wants to test, but cannot articulate resources she needs from others in an actionable way.

She is presented with the [Experiment Request Guide](https://labfellows.typeform.com/to/oCrUrA)

She now gets a chance to structure her ambiguous vision into a design of experiment broken down into three pieces: Protocols, Materials, and Labor. Based on the ERG, 3 events can happen through a logic tree: 

1. She answers all questions detailed and her ERG is completed and given a perfect score ranking so we know she can be matched easily by our sales team to do experiments herself in the right lab with right equipment, 
1. She completed ERG but skips several key questions she cannot answer so her ranking is low and ERG suggests consultation with our Experiment Specialist to fill in the gaps so she can be in the same place as 1 with perhaps some help from hiring our techs, or 
1. she sees the ERG and answers she already knows she wants to contract out her project and she may/may not need help from Experiment Specialist (depends on similar score ranking) developing protocols, materials, labor but definitely needs our Freelancers to execute.
