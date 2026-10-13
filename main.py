from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()

def main():
    print("Hello, LangChain!")
    information="""
    Donald John Trump (born June 14, 1946) is an American politician, media personality, and businessman who is the 47th president of the United States. A member of the Republican Party, he served as the 45th president from 2017 to 2021.

Born into a wealthy New York City family, Trump graduated from the University of Pennsylvania in 1968 with a bachelor's degree in economics. He became the president of his family's real estate business in 1971, renamed it the Trump Organization, and began acquiring and building skyscrapers, hotels, casinos, and golf courses. He launched side ventures, many licensing the Trump name, and filed for six business bankruptcies in the 1990s and 2000s. From 2004 to 2015, he hosted the reality television show The Apprentice, bolstering his reputation as a wealthy tycoon. Presenting himself as a political outsider, Trump won the 2016 presidential election against Democratic Party nominee Hillary Clinton.

During his first presidency, Trump imposed a travel ban on seven Muslim-majority countries, expanded the Mexico–United States border wall, and enforced a family separation policy on the border. He rolled back environmental and business regulations, signed the Tax Cuts and Jobs Act, and appointed three Supreme Court justices. He withdrew the U.S. from agreements on climate and trade and started a trade war with China. In response to the COVID-19 pandemic in 2020, he downplayed its severity, contradicted health officials, and signed the bipartisan CARES Act. After losing the 2020 presidential election to Joe Biden, Trump refused to concede defeat and attempted to overturn the result, resulting in the January 6 Capitol attack in 2021. He was impeached twice—in 2019 for abuse of power and obstruction of Congress and in 2021 for incitement of insurrection—and acquitted by the Senate both times.

In 2023, Trump was found liable in New York state civil cases for sexual abuse and defamation and for business fraud. In May 2024, he was found guilty in a New York state court on 34 counts of falsifying business records, making him the first U.S. president convicted of a felony. After winning the 2024 presidential election against Vice President Kamala Harris, he was given a no-penalty sentence, and two federal felony indictments for retention of classified documents and obstruction of the 2020 election were dismissed without prejudice.

Trump began his second presidency by initiating mass layoffs of federal workers. He imposed tariffs on nearly all countries at the highest level since the Great Depression and signed the One Big Beautiful Bill Act. His administration's actions—including the targeting of political opponents and civil society, restriction of transgender rights, mass deportation of undocumented immigrants, and extensive use of executive orders—have drawn over 550 lawsuits challenging their legality. In Latin America, he pursued a campaign to attack alleged drug traffickers and ordered a military raid into Venezuela to capture the country's president. In the Middle East, he authorized joint U.S.–Israeli strikes on Iran that began the 2026 Iran war.

Since 2015, Trump's leadership style and political agenda—often referred to as Trumpism—have reshaped the Republican Party's identity. Many of his comments and actions have been characterized as racist or misogynistic. He has made many false or misleading statements during his campaigns and presidency, to a degree unprecedented in American politics, and has promoted conspiracy theories. Trump's actions have been described by researchers as authoritarian and contributing to democratic backsliding. After his first term, scholars and historians ranked him as one of the worst presidents in American history."""
    
    
    summary_template = """
    Summarize the following information about Donald Trump in a concise manner, highlighting key points and significant events in his life and career:
    {information}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )
    
    llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0
)
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})

    print(response.content)

if __name__ == "__main__":
    main()