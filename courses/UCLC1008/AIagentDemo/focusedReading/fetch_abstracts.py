#!/usr/bin/env python3
"""
Fetch abstracts from Semantic Scholar API for all references in Ho et al. (2025).
Generates articles.csv with title, abstract, and relevance to the topic:
"The impact of AI chatbots and companion apps on humans"
"""

import csv
import time
import requests
import re

S2_API_KEY = "Rx2fP6Lcq833H9Dybfw3J38LfP0xYLaQ1T1f3BTc"
S2_SEARCH_URL = "https://api.semanticscholar.org/graph/v1/paper/search"

# All 104 references extracted from Ho et al. (2025) reference section
# Format: (ref_number, authors_short, year, title, is_included_in_review)
# is_included_in_review = True if marked with * in the paper
REFERENCES = [
    (1, "Abd-alrazaq et al.", 2019, "An overview of the features of chatbots in mental health: A scoping review", False),
    (2, "Aggarwal et al.", 2022, "Has the future started? The current growth of artificial intelligence, machine learning, and deep learning", False),
    (3, "Ahn and Shin", 2013, "Is the social use of media for seeking connectedness or for avoiding social isolation? Mechanisms underlying media use and subjective well-being", False),
    (4, "Alabed et al.", 2024, "More than just a chat: A taxonomy of consumers' relationships with conversational AI agents and their well-being implications", True),
    (5, "Aromataris et al.", 2014, "Methodology for JBI umbrella reviews", False),
    (6, "Baidoo-anu and Ansah", 2023, "Education in the era of generative artificial intelligence (AI): Understanding the potential benefits of ChatGPT in promoting teaching and learning", False),
    (7, "Balch", 2020, "AI and me: Friendship chatbots are on the rise, but is there a gendered design flaw?", False),
    (8, "Biondi et al.", 2023, "Editorial: Ethical design of artificial intelligence-based systems for decision making", False),
    (9, "Brey and Dainow", 2024, "Ethics by design for artificial intelligence", False),
    (10, "Brown and L'Engle", 2009, "X-rated: Sexual attitudes and behaviors associated with US early adolescents' exposure to sexually explicit media", False),
    (11, "Brun et al.", 2025, "Exploring Emotion-Sensitive LLM-Based Conversational AI", False),
    (12, "Buecker et al.", 2021, "Is loneliness in emerging adults increasing over time? A preregistered cross-temporal meta-analysis and systematic review", False),
    (13, "Calo", 2018, "Artificial intelligence policy: A primer and roadmap", False),
    (14, "Campbell et al.", 2019, "Lack of transparency in reporting narrative synthesis of quantitative data: A methodological assessment of systematic reviews", False),
    (15, "Cath", 2018, "Governing artificial intelligence: ethical, legal and technical opportunities and challenges", False),
    (16, "Chaturvedi et al.", 2023, "Social companionship with artificial intelligence: Recent trends and future avenues", False),
    (17, "Chaturvedi et al.", 2024, "Empowering AI companions for enhanced relationship marketing", True),
    (18, "Chen et al.", 2024, "Design of artificial intelligence companion chatbot", False),
    (19, "Chin et al.", 2023, "The Potential of Chatbots for Emotional Support and Promoting Mental Well-Being in Different Cultures: Mixed Methods Study", False),
    (20, "Ciriello et al.", 2024, "Ethical tensions in human-ai companionship: A dialectical inquiry into replika", True),
    (21, "Cotten et al.", 2013, "Impact of internet use on loneliness and contact with others among older adults: Cross-sectional analysis", False),
    (22, "De Angelis et al.", 2023, "ChatGPT and the rise of large language models: The new AI-driven infodemic threat in public health", False),
    (23, "Diaa et al.", 2024, "Statistical Challenges in Social Media Data Analysis Sentiment Tracking and Beyond", False),
    (24, "Depounti et al.", 2023, "Ideal technologies, ideal women: AI and gender imaginaries in Redditors' discussions on the Replika bot girlfriend", True),
    (25, "Dewitte", 2024, "Better alone than in bad company: Addressing the risks of companion chatbots through data protection by design", True),
    (26, "Di Natale et al.", 2023, "Uncanny valley effect: A qualitative synthesis of empirical research to assess the suitability of using virtual faces in psychological research", False),
    (27, "Fraune et al.", 2022, "Socially facilitative robots for older adults to alleviate social isolation: A participatory design workshop approach in the US and Japan", False),
    (28, "Freitas et al.", 2024, "AI Companions Reduce Loneliness", False),
    (29, "Gao et al.", 2018, "Alexa, My Love: Analyzing reviews of amazon echo", True),
    (30, "Gatti et al.", 2016, "SentiWords: Deriving a High Precision and High Coverage Lexicon for Sentiment Analysis", False),
    (31, "George et al.", 2023, "A review of ChatGPT AI's impact on several business sectors", False),
    (32, "Guingrich and Graziano", 2023, "Chatbots as social companions: How people perceive consciousness, human likeness, and social health benefits in machines", False),
    (33, "Hartanto et al.", 2024, "Cultural contexts differentially shape parents' loneliness and wellbeing during the empty nest period", False),
    (34, "Heilinger", 2022, "The Ethics of AI Ethics. A Constructive Critique", False),
    (35, "Helsper and Smahel", 2020, "Excessive internet use by young Europeans: psychological vulnerability and digital literacy?", False),
    (36, "Hernandez-Ortega and Ferreira", 2021, "How smart experiences build service loyalty: The importance of consumer love for smart voice assistants", True),
    (37, "Heymans and Heyman", 2024, "Identifying stakeholder motivations in normative AI governance: a systematic literature review for research guidance", False),
    (38, "Hollebeek et al.", 2024, "Engaging consumers through artificially intelligent technologies: Systematic review, conceptual model, and further research", False),
    (39, "Holdier and Weirich", 2025, "AI Romance and Misogyny: A Speech Act Analysis", False),
    (40, "Holt-Lunstad et al.", 2017, "Advancing social connection as a public health priority in the United States", False),
    (41, "Hosseini et al.", 2024, "Formulating research questions for evidence-based studies", False),
    (42, "Hu", 2023, "ChatGPT sets record for fastest-growing user base—Analyst note", False),
    (43, "Hu et al.", 2024, "AI as your ally: The effects of AI-assisted venting on negative affect and perceived social support", False),
    (44, "Imran and Almusharraf", 2024, "Google Gemini as a next generation AI educational tool: a review of emerging educational technology", False),
    (45, "Jecker et al.", 2024, "Digital humans to combat loneliness and social isolation: Ethics concerns and policy recommendations", True),
    (46, "Jiang et al.", 2022, "Chatbot as an emergency exist: Mediated empathy for resilience via human-AI interaction during the COVID-19 pandemic", False),
    (47, "Johnson", 2023, "WHO declares loneliness a 'global public health concern'", False),
    (48, "Kacar", 2023, "The role of online communication platforms in maintaining social connectedness when face-to-face communication is restricted", False),
    (49, "Karaboga and Vardarlier", 2020, "Examining the use of artificial intelligence in recruitment processes", False),
    (50, "Kim et al.", 2023, "Investigating the importance of social presence on intentions to adopt an AI romantic partner", False),
    (51, "Kirkham et al.", 2013, "Can a core outcome set improve the quality of systematic reviews?--a survey of the Co-ordinating Editors of Cochrane Review Groups", False),
    (52, "Koulouri et al.", 2022, "Chatbots to Support Young Adults' Mental Health: An Exploratory Study of Acceptability", False),
    (53, "Kouros and Papa", 2024, "Digital Mirrors: AI Companions and the Self", False),
    (54, "Kumar and Sangwan", 2024, "Conceptualizing AI Literacy: Educational and Policy Initiatives for a Future-Ready Society", False),
    (55, "Laestadius et al.", 2022, "Too human and not human enough: A grounded theory analysis of mental health harms from emotional dependence on the social chatbot Replika", True),
    (56, "Lee", 2023, "I thought I'd found friendship with a Replika AI chatbot", False),
    (57, "Lee et al.", 2021, "Social interactions and relationships with an intelligent virtual agent", False),
    (58, "Li et al.", 2022, "Does the internet bring people closer together or further apart? The impact of internet usage on interpersonal communications", False),
    (59, "Li and Zhang", 2024, "Finding love in algorithms: Deciphering the emotional contexts of close encounters with AI chatbots", True),
    (60, "Liu et al.", 2024, "Chatbot Companionship: A Mixed-Methods Study of Companion Chatbot Usage Patterns and Their Relationship to Loneliness in Active Users", False),
    (61, "Liberati", 2023, "Digital Intimacy in China and Japan: A Phenomenological and Postphenomenological Perspective on Love Relationships at the Time of Digital Technologies in China and Japan", False),
    (62, "Limna et al.", 2023, "The use of ChatGPT in the digital era: Perspectives on chatbot implementation", False),
    (63, "Long and Magerko", 2020, "What is AI Literacy? Competencies and Design Considerations", False),
    (64, "Luckin et al.", 2016, "Intelligence Unleashed: An argument for AI in education", False),
    (65, "McStay", 2023, "Replika in the Metaverse: The moral problem with empathy in 'It from Bit'", False),
    (66, "Merrill et al.", 2022, "AI companions for lonely individuals and the role of social presence", False),
    (67, "Mhlanga", 2023, "Open AI in education, the responsible and ethical use of ChatGPT towards lifelong learning", False),
    (68, "Mittelstadt et al.", 2016, "The ethics of algorithms: Mapping the debate", False),
    (69, "Moher et al.", 2009, "Preferred reporting items for systematic reviews and meta-analyses: The PRISMA statement", False),
    (70, "Mubassira et al.", 2024, "Enhancing EmoBot: An In-Depth Analysis of User Satisfaction and Faults in an Emotion-Aware Chatbot", False),
    (71, "Murthy et al.", 2021, "Individually vulnerable, collectively safe: The security and privacy practices of households with older adults", False),
    (72, "Nadarzynski et al.", 2019, "Acceptability of artificial intelligence (AI)-led chatbot services in healthcare: A mixed-methods study", False),
    (73, "Olson", 2018, "This AI Has Sparked A Budding Friendship With 2.5 Million People", False),
    (74, "Oertel et al.", 2020, "Engagement in Human-Agent Interaction: An Overview", False),
    (75, "Pal et al.", 2023, "What affects the usage of artificial conversational agents? An agent personality and love theory perspective", True),
    (76, "Pan et al.", 2023, "Desirable or distasteful? Exploring uncertainty in human-chatbot relationships", True),
    (77, "Pentina et al.", 2023, "Exploring relationship development with social chatbots: A mixed-method study of replika", False),
    (78, "Pentina et al.", 2023, "Consumer-machine relationships in the age of artificial intelligence: Systematic literature review and research directions", False),
    (79, "Placani", 2024, "Anthropomorphism in AI: Hype and fallacy", False),
    (80, "Primack et al.", 2017, "Social media use and perceived social isolation among young adults in the U.S", False),
    (81, "Prochazka and Brooks", 2024, "Digital lovers and jealousy: Anticipated emotional responses to emotionally and physically sophisticated sexual technologies", True),
    (82, "Ragab et al.", 2024, "'Trust me over my privacy policy': Privacy discrepancies in romantic ai chatbot apps", True),
    (83, "Rao et al.", 2023, "Assessing the utility of ChatGPT throughout the entire clinical workflow: Development and usability study", False),
    (84, "Pettman", 2009, "Love in the Time of Tamagotchi", True),
    (85, "Rodriguez-Martinez et al.", 2024, "Qualitative Analysis of Conversational Chatbots to Alleviate Loneliness in Older Adults as a Strategy for Emotional Health", False),
    (86, "Root", 2024, "Reconfiguring the alterity relation: The role of communication in interactions with social robots and chatbots", True),
    (87, "Sharma", 2024, "Benefits or concerns of AI: A multistakeholder responsibility", False),
    (88, "Siahaan and Wulan", 2024, "The Influence of Interpersonal Communication on Relational Commitment in Young Married Couples in Indonesia", False),
    (89, "Siemon et al.", 2022, "Why do we turn to virtual companions? A text mining analysis of Replika reviews", True),
    (90, "Skjuve et al.", 2023, "A longitudinal study of self-disclosure in human-chatbot relationships", True),
    (91, "Skjuve et al.", 2021, "My chatbot companion - A study of human-chatbot relationships", True),
    (92, "Sternberg", 1986, "A triangular theory of love", False),
    (93, "Sullivan et al.", 2023, "Combating loneliness with artificial intelligence: An AI-based emotional support model", False),
    (94, "Ta et al.", 2020, "User experiences of social support from companion chatbots in everyday contexts: Thematic analysis", False),
    (95, "Takats et al.", 2023, "Zotero (6.0.37) [MacOS]", False),
    (96, "UNESCO", 2021, "Recommendation on the ethics of artificial intelligence", False),
    (97, "Vasilescu and Gheorghe", 2024, "Improving the Performance of Corporate Employees through the Use of Artificial Intelligence: The Case of Copilot Application", False),
    (98, "Song et al.", 2010, "Dissemination and publication of research findings: an updated review of related biases", False),
    (99, "Wygnanska", 2023, "The experience of conversation and relation with a well-being chatbot: Between proximity and remoteness", True),
    (100, "Xie and Pentina", 2022, "Attachment theory as a framework to understand relationships with social chatbots: A case study of Replika", True),
    (101, "Xie et al.", 2023, "Friend, mentor, lover: Does chatbot engagement lead to psychological dependence?", True),
    (102, "Yoganathan et al.", 2021, "Check-in at the Robo-desk: Effects of automated social presence on social cognition and service implications", False),
    (103, "Zhang et al.", 2024, "The Dark Side of AI Companionship: A Taxonomy of Harmful Algorithmic Behaviors in Human-AI Relationships", False),
    (104, "Zheng et al.", 2025, "Customizing Emotional Support: How Do Individuals Construct and Interact With LLM-Powered Chatbots", False),
]


# Keywords for relevance classification
RELEVANCE_KEYWORDS = [
    "chatbot", "companion", "ai companion", "conversational agent", "social chatbot",
    "replika", "emotional support", "loneliness", "well-being", "wellbeing",
    "mental health", "human-chatbot", "human-ai", "ai relationship",
    "romantic", "attachment", "anthropomorphism", "social robot",
    "digital companion", "virtual companion", "ai friend", "emotional dependence",
    "psychological", "self-disclosure", "empathy", "social presence",
    "privacy", "ethical", "user experience", "sentiment",
]


def search_semantic_scholar(title, api_key):
    """Search Semantic Scholar for an article by title and return the abstract."""
    headers = {
        "x-api-key": api_key,
    }
    params = {
        "query": title,
        "limit": 3,
        "fields": "title,abstract,year,venue,citationCount,externalIds",
    }

    try:
        resp = requests.get(S2_SEARCH_URL, headers=headers, params=params, timeout=15)
        resp.raise_for_status()
        data = resp.json()

        papers = data.get("data", [])
        if papers:
            # Try to find best match by comparing titles
            best_match = None
            best_score = 0
            title_lower = title.lower().strip()

            for paper in papers:
                paper_title = (paper.get("title") or "").lower().strip()
                # Simple similarity: ratio of matching words
                title_words = set(re.findall(r'\w+', title_lower))
                paper_words = set(re.findall(r'\w+', paper_title))
                if not title_words:
                    continue
                overlap = len(title_words & paper_words)
                score = overlap / max(len(title_words), len(paper_words))
                if score > best_score:
                    best_score = score
                    best_match = paper

            if best_match and best_score > 0.5:
                abstract = best_match.get("abstract") or "No abstract available"
                venue = best_match.get("venue") or ""
                citations = best_match.get("citationCount", "")
                ext_ids = best_match.get("externalIds") or {}
                doi = ext_ids.get("DOI", "")
                return {
                    "s2_title": best_match.get("title", ""),
                    "abstract": abstract,
                    "journal": venue,
                    "doi": doi,
                    "citations": citations,
                    "found": True,
                    "match_score": round(best_score, 2),
                }

        return {
            "s2_title": "",
            "abstract": "Not found in Semantic Scholar",
            "journal": "",
            "doi": "",
            "citations": "",
            "found": False,
            "match_score": 0,
        }
    except Exception as e:
        return {
            "s2_title": "",
            "abstract": f"Error: {str(e)}",
            "journal": "",
            "doi": "",
            "citations": "",
            "found": False,
            "match_score": 0,
        }


def classify_relevance(title, abstract):
    """Classify whether an article is directly relevant to the topic."""
    text = (title + " " + abstract).lower()
    matched_keywords = []

    for kw in RELEVANCE_KEYWORDS:
        if kw.lower() in text:
            matched_keywords.append(kw)

    has_ai_chatbot = any(
        kw in text
        for kw in [
            "chatbot", "companion", "conversational agent", "replika",
            "social robot", "virtual companion", "digital companion",
            "ai companion", "voice assistant",
        ]
    )
    has_human_impact = any(
        kw in text
        for kw in [
            "loneliness", "well-being", "wellbeing", "mental health",
            "emotional", "psychological", "attachment", "self-disclosure",
            "relationship", "social presence", "empathy", "privacy",
            "user experience", "dependence", "romantic", "love",
        ]
    )

    if has_ai_chatbot and has_human_impact:
        relevance = "Directly relevant"
    elif has_ai_chatbot or (len(matched_keywords) >= 3 and has_human_impact):
        relevance = "Potentially relevant"
    else:
        relevance = "Not directly relevant"

    return relevance, matched_keywords


def main():
    output_file = "articles.csv"
    total = len(REFERENCES)

    print(f"Starting Semantic Scholar API queries for {total} references...")
    print(f"Rate limit: 1 req/sec — estimated time: ~{total * 1.2:.0f} seconds")
    print("=" * 80)

    rows = []
    found_count = 0
    relevant_count = 0

    for i, (ref_num, authors, year, title, in_review) in enumerate(REFERENCES):
        print(f"[{i+1}/{total}] Ref #{ref_num}: {authors} ({year})")
        print(f"  Title: {title[:80]}{'...' if len(title) > 80 else ''}")

        # Skip non-article entries
        if title.startswith("Zotero"):
            result = {
                "s2_title": "", "abstract": "Software tool - not an article",
                "journal": "", "doi": "", "citations": "", "found": False, "match_score": 0,
            }
        else:
            result = search_semantic_scholar(title, S2_API_KEY)
            # Rate limit: 1 request per second
            time.sleep(1.05)

        if result["found"]:
            found_count += 1
            print(f"  -> Found (score={result['match_score']})")
        else:
            print(f"  -> {result['abstract'][:80]}")

        relevance, keywords = classify_relevance(title, result.get("abstract", ""))
        if relevance == "Directly relevant":
            relevant_count += 1
            print(f"  ** {relevance} (keywords: {', '.join(keywords[:5])})")

        rows.append({
            "ref_number": ref_num,
            "authors": authors,
            "year": year,
            "title": title,
            "s2_title": result.get("s2_title", ""),
            "abstract": result.get("abstract", ""),
            "journal": result.get("journal", ""),
            "doi": result.get("doi", ""),
            "citations": result.get("citations", ""),
            "in_review": "Yes" if in_review else "No",
            "relevance": relevance,
            "matched_keywords": "; ".join(keywords),
            "found_in_s2": "Yes" if result["found"] else "No",
            "match_score": result.get("match_score", 0),
        })

        # Progress report every 20 articles
        if (i + 1) % 20 == 0:
            print(f"\n  --- Progress: {i+1}/{total} done | {found_count} found | {relevant_count} directly relevant ---\n")

    # Write CSV
    fieldnames = [
        "ref_number", "authors", "year", "title", "s2_title", "abstract",
        "journal", "doi", "citations", "in_review", "relevance",
        "matched_keywords", "found_in_s2", "match_score",
    ]

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print("\n" + "=" * 80)
    print(f"DONE! Results written to {output_file}")
    print(f"Total references: {total}")
    print(f"Found in Semantic Scholar: {found_count}")
    print(f"Directly relevant to topic: {relevant_count}")
    print(f"Potentially relevant: {sum(1 for r in rows if r['relevance'] == 'Potentially relevant')}")
    print(f"Not directly relevant: {sum(1 for r in rows if r['relevance'] == 'Not directly relevant')}")

    # Print summary of directly relevant articles
    print("\n" + "=" * 80)
    print("DIRECTLY RELEVANT ARTICLES:")
    print("=" * 80)
    for r in rows:
        if r["relevance"] == "Directly relevant":
            in_rev = " [IN REVIEW]" if r["in_review"] == "Yes" else ""
            print(f"\n  [{r['ref_number']}] {r['authors']} ({r['year']}){in_rev}")
            print(f"  {r['title']}")
            abs_text = r['abstract']
            if abs_text and abs_text not in ("Not found in Semantic Scholar", "Software tool - not an article"):
                print(f"  Abstract: {abs_text[:200]}...")

    print("\n" + "=" * 80)
    print("POTENTIALLY RELEVANT ARTICLES:")
    print("=" * 80)
    for r in rows:
        if r["relevance"] == "Potentially relevant":
            in_rev = " [IN REVIEW]" if r["in_review"] == "Yes" else ""
            print(f"\n  [{r['ref_number']}] {r['authors']} ({r['year']}){in_rev}")
            print(f"  {r['title']}")


if __name__ == "__main__":
    main()
