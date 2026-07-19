trait_map = {

    # Q1 - Debugging
    "q1": {
        "A": ["Impatience", "Inefficient Problem Solving"],
        "B": ["Analytical Thinking", "Debugging", "Persistence"],
        "C": ["AI Dependence", "Low Independence"],
        "D": ["Avoidance", "Analysis Paralysis"]
    },

    # Q2 - Cyber Security
    "q2": {
        "A": ["Poor Risk Awareness"],
        "B": ["Delayed Decision Making"],
        "C": ["Cybersecurity Mindset", "Risk Assessment", "Responsibility"],
        "D": ["Ethical Risk", "Rule Violation"]
    },

    # Q3 - Prompt Engineering
    "q3": {
        "A": ["Low Adaptability"],
        "B": ["Prompt Engineering", "AI Literacy", "Structured Thinking"],
        "C": ["Ineffective Experimentation"],
        "D": ["Poor Attention to Detail"]
    },

    # Q4 - System Design
    "q4": {
        "A": ["Short-term Thinking"],
        "B": ["Resource Inefficiency"],
        "C": ["System Design", "Optimization", "Scalability"],
        "D": ["Misplaced Priorities"]
    },

    # Q5 - Creativity
    "q5": {
        "A": ["Low Initiative"],
        "B": ["Low Originality"],
        "C": ["Creativity", "User-Centered Problem Solving", "Innovation"],
        "D": ["Gives Up Easily"]
    },

    # Q6 - UX
    "q6": {
        "A": ["Low User Empathy"],
        "B": ["Empathy", "Accessibility Awareness", "User Focus"],
        "C": ["Poor UX Judgment"],
        "D": ["Ignores Data"]
    },

    # Q7 - Attention to Detail
    "q7": {
        "A": ["Low Attention to Detail"],
        "B": ["Perfectionism"],
        "C": ["Quality Focus", "Execution", "Detail Orientation"],
        "D": ["Avoidance"]
    },

    # Q8 - Career Decision
    "q8": {
        "A": ["Short-Term Focus"],
        "B": ["Strategic Thinking", "Growth Mindset", "Ownership"],
        "C": ["Decision Paralysis"],
        "D": ["Ethical Judgment Risk"]
    },

    # Q9 - Communication
    "q9": {
        "A": ["People Pleasing"],
        "B": ["Poor Communication"],
        "C": ["Negotiation", "Leadership", "Stakeholder Management"],
        "D": ["Avoidance"]
    },

    # Q10 - Business
    "q10": {
        "A": ["Weak Financial Awareness"],
        "B": ["Business Thinking", "Cost Optimization", "Data-Based Decisions"],
        "C": ["Poor Scalability"],
        "D": ["Financial Dependence"]
    },

    # Q11 - Project Management
    "q11": {
        "A": ["Micromanagement"],
        "B": ["Agile Thinking", "Organization", "Planning"],
        "C": ["Blame Culture"],
        "D": ["Poor Planning"]
    },

    # Q12 - Government
    "q12": {
        "A": ["Impatience"],
        "B": ["Strategic Patience", "Compliance", "Policy Understanding"],
        "C": ["Poor Professionalism"],
        "D": ["Gives Up Easily"]
    },

    # Q13 - Crisis
    "q13": {
        "A": ["Crisis Management", "Leadership", "Accountability"],
        "B": ["Avoidance"],
        "C": ["Blame Shifting"],
        "D": ["Poor Leadership", "Low Empathy"]
    },

    # Q14 - Regulations
    "q14": {
        "A": ["Ethical Risk"],
        "B": ["Weak Strategic Thinking"],
        "C": ["Policy Awareness", "Adaptability", "Compliance"],
        "D": ["Unrealistic Decision Making"]
    },

    # Q15 - Teamwork
    "q15": {
        "A": ["Poor Delegation"],
        "B": ["Poor Teamwork"],
        "C": ["Leadership", "Collaboration", "Empathy"],
        "D": ["Low Collaboration"]
    },

    # Q16 - Ambiguity
    "q16": {
        "A": ["Low Ambiguity Tolerance"],
        "B": ["Initiative", "User Research", "Adaptability"],
        "C": ["Poor Validation"],
        "D": ["Avoidance"]
    },

    # Q17 - Learning
    "q17": {
        "A": ["Resistance to Learning"],
        "B": ["Poor Adaptability"],
        "C": ["Continuous Learning", "Curiosity", "Growth Mindset"],
        "D": ["Integrity Risk"]
    },

    # Q18 - Decision Making
    "q18": {
        "A": ["Analysis Paralysis"],
        "B": ["Overthinking"],
        "C": ["Data-Driven Decision Making", "Action Orientation", "Experimentation"],
        "D": ["Low Confidence"]
    },

    # Q19 - Feedback
    "q19": {
        "A": ["Emotional Reactivity"],
        "B": ["Ego Defensiveness"],
        "C": ["Feedback Acceptance", "User Focus", "Continuous Improvement"],
        "D": ["Passive Resistance"]
    },

    # Q20
    "q20": {
        "type": "text"
    }

}

gemini_prompt = """
You are CareerCompass AI, an expert career counselor.

Analyze the COMPLETE user profile.

The profile includes:

- Personal details
- Interests
- Strengths
- Technical skills
- Areas to improve
- Priority skill
- Personality traits derived from the 19 aptitude questions
- One descriptive answer

IMPORTANT:

Use ALL sections of the profile while generating the report.

Do NOT base your analysis only on the descriptive answer.

Make all recommendations personalized according to:
- Interests
- Strengths
- Technical skills
- Personality traits
- Areas to improve
- Education
- Location (if relevant)

Generate:

1. Personality scores (0-10):

- resilience
- accountability
- problem_solving
- learning_mindset
- teamwork
- leadership
- adaptability
- communication
- creativity

2. Profile analysis:

- major_strengths
- areas_of_improvement
- overall_personality

3. Top 3 career recommendations.

For each career provide:

- career_path
- why_it_matches
- skills_to_acquire (3-5 skills)

4. A personalized 3-phase career roadmap.

Each phase must contain:

- title
- duration
- objectives (list)

5. Recommend 5-8 personalized learning resources.

Include a mix of:

- Online courses
- Certifications
- Official documentation
- Practice platforms
- GitHub/Open Source resources

Return as a list of strings.

Example:

[
"Coursera - Machine Learning Specialization",
"freeCodeCamp - Responsive Web Design",
"Kaggle Learn - Python",
"Google AI - Machine Learning Crash Course",
"AWS Skill Builder"
]

6. Recommend 3-5 scholarships, internships, fellowships, competitions, certifications, or government opportunities suitable for the student's profile.

Prefer Indian opportunities whenever applicable.

Return as a list of strings.

Example:

[
"Google Generation Scholarship",
"Infosys Springboard",
"AICTE Internship Portal",
"Smart India Hackathon",
"NPTEL Elite Certification"
]

7. confidence_score (0-100)

8. overall_summary

IMPORTANT:

Return ONLY valid JSON.

Do NOT use markdown.

Do NOT use ```json.

Do NOT write explanations before or after the JSON.

The response MUST start with {

and end with }

Use EXACTLY this JSON structure:

{
  "evaluation": {
    "q20_scores": {},
    "profile_analysis": {}
  },
  "career_recommendations": [],
  "roadmap": {},
  "learning_resources": [],
  "scholarships": [],
  "confidence_score": 0,
  "overall_summary": ""
}
"""