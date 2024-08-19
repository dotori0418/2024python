import  wikipedia
# wiki=wikipedia.page('Artificial intelligece')
# text=wiki.content
text="""Martin Luther King Jr. (born Michael King Jr.; January 15, 1929 – April 4, 1968) was an American Christian minister, activist, and political philosopher who was one of the most prominent leaders in the civil rights movement from 1955 until his assassination in 1968. A Black church leader and a son of early civil rights activist and minister Martin Luther King Sr., King advanced civil rights for people of color in the United States through the use of nonviolent resistance and nonviolent civil disobedience against Jim Crow laws and other forms of legalized discrimination.

King participated in and led marches for the right to vote, desegregation, labor rights, and other civil rights.[1] He oversaw the 1955 Montgomery bus boycott and later became the first president of the Southern Christian Leadership Conference (SCLC). As president of the SCLC, he led the unsuccessful Albany Movement in Albany, Georgia, and helped organize some of the nonviolent 1963 protests in Birmingham, Alabama. King was one of the leaders of the 1963 March on Washington, where he delivered his "I Have a Dream" speech on the steps of the Lincoln Memorial, and helped organize two of the three Selma to Montgomery marches during the 1965 Selma voting rights movement. The civil rights movement achieved pivotal legislative gains in the Civil Rights Act of 1964, Voting Rights Act of 1965, and the Fair Housing Act of 1968.

The SCLC put into practice the tactics of nonviolent protest with some success by strategically choosing the methods and places in which protests were carried out. There were several dramatic standoffs with segregationist authorities, who frequently responded violently.[2] King was jailed several times. Federal Bureau of Investigation (FBI) director J. Edgar Hoover considered King a radical and made him an object of the FBI's COINTELPRO from 1963 forward. FBI agents investigated him for possible communist ties, spied on his personal life, and secretly recorded him. In 1964, the FBI mailed King a threatening anonymous letter, which he interpreted as an attempt to make him commit suicide.[3]

On October 14, 1964, King won the Nobel Peace Prize for combating racial inequality through nonviolent resistance. In his final years, he expanded his focus to include opposition towards poverty and the Vietnam War. In 1968, King was planning a national occupation of Washington, D.C., to be called the Poor People's Campaign, when he was assassinated on April 4 in Memphis, Tennessee. James Earl Ray, a fugitive from the Missouri State Penitentiary, was convicted of the assassination, though the King family believes he was a scapegoat; the assassination remains the subject of conspiracy theories. King's death was followed by national mourning, as well as anger leading to riots in many U.S. cities. King was posthumously awarded the Presidential Medal of Freedom in 1977 and the Congressional Gold Medal in 2003. Martin Luther King Jr. Day was established as a holiday in cities and states throughout the United States beginning in 1971; the federal holiday was first observed in 1986. Hundreds of streets in the U.S. have been renamed in his honor, and King County in Washington was rededicated for him. The Martin Luther King Jr. Memorial on the National Mall in Washington, D.C., was dedicated in 2011."""
print(text)


from wordcloud import WordCloud
wd=WordCloud(width =2000, height = 1500).generate(text)


import matplotlib.pyplot as plt
plt.figure(figsize=(10, 8))
plt.axis('off')
plt.imshow(wd)
plt.show()
# =========================================이재묵20122=========================================