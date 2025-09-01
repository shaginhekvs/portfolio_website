# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Personal information
    personal_info = {
        'name': 'Keshav Singh',
        'title': 'Curious computer jigzaw puzzle solver',
        'location': 'Zurich, Switzerland',
        'phone': '+41 77436 1338',
        'email': 'to.keshav.singh@gmail.com',
        'linkedin': 'linkedin.com/in/keshav-singh-900472148/',
        'github': 'github.com/shaginhekvs'
    }
    
    # Summary
    summary = """Passionate software engineer with a strong experience (>5 years) in oci cloud architecture, SQL, GPU kernel optimization, spark query optimization, machine learning, generative AI, 
    database systems features design, development and debugging. Skilled in C++, SQL, Python, PyTorch, and various ML
    libraries. Excellent problem-solving, research, and collaboration abilities. Seeking an impactful role at
    the intersection of cloud architecture, query processing, AI and machine learning."""
    
    # Technical Skills
    technical_skills = {
        'Programming Languages and tools': ['C++', 'SQL', 'Python', 'Java', 'Git', 'Jenkins', 'Shell', 'CMake'],
        'ML Frameworks': ['PyTorch', 'Keras', 'Scikit-learn', 'Langchain', 'Langgraph', 'Spark-ML', 'Crew AI'],
        'Data tools': ['Palantir Foundry', 'Databricks', 'Oracle DB', 'MySQL HeatWave', 'Airflow', 'Dataiku', 'Neo4J', 'MS SQL Server', 'AWS Aurora']
    }
    
    # Experience
    experience = [
        {
            'title': 'Senior Member of Technical Staff',
            'company': 'Oracle MySQL HeatWave Optimizer Team',
            'location': 'Zurich, Switzerland',
            'duration': 'May 2022 – Present',
            'achievements': [
                'Enhancing Optimizer for MySQL Heatwave leading to performance gains upto 27x in various analytics database system benchmarks: JOB, TPCH, TPCDS using machine learning and algorithmic techniques. Languages used: C++, Python, Java and Shell.',
                'SDE tasks with various Oracle Cloud Infra components: compute, linux OS, object store, qemu-KVM, Networking(VNC, RoCE, Ethernet), IAM.',
                'Developing MySQL-AI Enterprise Release feature of Chain of Thought reasoning on relational data using LangChain.',
                'Benchmarking and optimization of MySQL heatwave query processing performance on latest ARM architecture. Optimizations involved process NUMA locality, L3 Cache-use optimization, instruction pre-fetching optimization.',
                'Performing peer code reviews and feature design reviews.',
                'Successfully applied to 2 US Patent applications (currently under processing) in the area of applying Machine Learning methods for query optimization.',
                'Development and deployment of machine learning models for cardinality estimation, query optimization decisions.',
                'Testing infrastructure enhancements using Git, Jenkins, Java and Python.',
                'Mentoring Interns and and new members of query processing team.'
            ]
        },
        {
            'title': 'Data Scientist Consultant',
            'company': 'Unit8',
            'location': 'Lausanne, Switzerland',
            'duration': 'Feb 2021 – April 2022',
            'achievements': [
                'Developed scalable data pipelines (up-to billion records) and robust data ontology for client using PySpark, ElasticSearch, Palantir Foundry, MS SQL Server for dashboards used by CEO, CFO , MDs and 1000s of analysts at Swiss Re.',
                'Developed AI and ML models for various client usecases like pricing models for reinsurance contracts using hierarchical encoding, xgboost model.',
                'Developed Model Catalog for AI Center of Excellence at Swiss Re leveraging Palantir Model auto-registry, Slate dashboard. Dashboard used as main hub of model governance and approvals.',
                'Data platform architecture design and review for Julius Baer, identifying current and potential future scalability, usability and reliability, and suggesting architecture changes needed. Final solution leverages Apache Calcite, Hive, Iceberg, Dataiku.'
            ]
        },
        {
            'title': 'Data Science Intern',
            'company': 'Credit Suisse',
            'location': 'Lausanne, Switzerland',
            'duration': 'March 2020 – Aug 2020',
            'achievements': [
                'Developed and deployed graph machine learning models for financial compliance and fraud detection using Python, Palantir Foundry, Pyspark, Neo4J.',
                'Improving AML models using Graph Machine learning, and feature extraction on knowledge graphs build on neo4j via DeepWalk and Node2Vec. '
            ]
        },
        {
            'title': 'Deep Learning Engineer (Part Time)',
            'company': 'Siemens Healthineers',
            'location': 'Lausanne, Switzerland',
            'duration': 'July 2019 – Feb 2020',
            'achievements': [
                'Research and development of ML based pipeline for calculation of mean upper cervical cord area from MRI images. Developed a E2E pipeline using Image segmentation and classification tasks using InceptionResnet Model with custom loss function based on DICE and FOCAL loss functions, with a high IOU score in the final output',
                'Summer Deep Learning Research Intern from July - September 2019 Hyper parameter optimization of deep machine learning models aimed at better medical diagnosis using MRI images as datasets.',
                'Project integrated in Siemens pipeline and led to improvement of a clinical segmentation network by 10%.'
            ]
        },
        {
            'title': 'Quantitative Developer',
            'company': 'CIGP',
            'location': 'Hong Kong, Geneva, Switzerland',
            'duration': 'March 2018 – Feb 2019',
            'achievements': [
                'Joined Asset Management team as full time intern from March - September, then part time until Feb for researching and implementing the following: 1. Efficient Frontier Optimization of Portfolios by using Statistical Optimization Methods with Market Pricing Data, 2. Deep Sentiment Analysis of Large Cap US equities using News Corpus. 3. Deep Q Reinforcement learning for Optimal Portfolio Allocation'
            ]
        }
    ]
    
    # Education
    education = [
        {
            'degree': 'M.S. in Communication Systems',
            'school': 'EPFL',
            'location': 'Lausanne, Switzerland',
            'duration': 'Aug 2017 – Feb 2021',
            'gpa': '5.45/6 GPA'
        },
        {
            'degree': 'B.S. in Electrical Engineering and Computer Science',
            'school': 'City University of Hong Kong',
            'location': 'Hong Kong',
            'duration': 'Aug 2013 – May 2017',
            'gpa': '4.1/4.3 GPA'
        }
    ]
    
    # Projects
    projects = [
        
        {
            'name': 'NxTreasury',
            'role': 'Technical Advisor',
            'duration': '2024/2025',
            'technologies': 'Python, vLLM, Crew AI, Langgraph',
            'description': 'Web development of https://www.nxtreasury.com using bootstrap, ReactJS frontend, Python flask backend. Integration with web3 ethereum blockchain for transaction execution. Architecture setup, devops deployment using Github Actions, Azure Webapps. Finetuning LLM using AWS for financial contract management on AWS using CoT reasoning using langgchain. Deploying Agents fleet for transactions execution, risk screening using crew AI and laggraph. Successfully applied for and awarded Azure Startup grant, NVIDIA startup grant, AWS Activate grant. Watch the demo video at  https://www.youtube.com/watch?v=9w6u0tVnlAs',
            'github': 'https://www.nxtreasury.com'
        },
        {
            'name': 'CUDA TUTORIALS',
            'role': 'Personal project',
            'duration': '2024/2025',
            'technologies': 'CUDA, CUBLAS',
            'description': 'Tutorials for learning CUDA, both SM based execution and tensor based execution.',
            'github': 'https://github.com/shaginhekvs/CUDA-Tutorial'
        },
        {
            'name': 'Metoo Analysis',
            'role': 'Student project',
            'duration': '2018',
            'technologies': 'Python, Spark',
            'description': 'Big Data Analysis using Spark to analyze metoo movement on twitter.',
            'github': 'https://shaginhekvs.github.io/ada_course/'
        },
        {
            'name': 'ChatBot',
            'role': 'Student project',
            'duration': '2018',
            'technologies': 'Python, LLMs',
            'description': 'Building a chatbot by using sequence to sequence ML model implemented with Transformer.',
            'github': 'https://github.com/shaginhekvs/ANNproject'
        },
        {
            'name': 'AggMo',
            'role': 'Student project',
            'duration': '2020',
            'technologies': 'Python, Pytorch',
            'description': 'Implementing a Machine Learning framework using PyTorch with a custom optimizer AggMo.',
            'github': 'https://github.com/shaginhekvs/DL_Project'
        },
        {
            'name': 'NSM operators',
            'role': 'Student project',
            'duration': '2019',
            'technologies': 'Java',
            'description': 'Implementing NSM, DSM database storage systems in Java and associated operators.',
            'github': 'https://github.com/shaginhekvs/CS422-Project1'
        },
        {
            'name': 'Cube operators',
            'role': 'Student project',
            'duration': '2020',
            'technologies': 'Java, Scala',
            'description': 'Implementing Cube operator, similarity join operations using Spark in Scala, to operate efficiently on huge datasets.',
            'github': 'https://github.com/shaginhekvs/CS422-Project2-Private'
        },
        {
            'name': 'Vote Graphs',
            'role': 'Student project',
            'duration': '2019',
            'technologies': 'Python, Graphs',
            'description': 'Using Transductive learning and Signal Processing on Graphs to predict votes of US senators.',
            'github': 'https://github.com/lkieliger/US-Senators'
        }

    ]
    
    # Publications
    publications = [
        {
            'title': 'MGSAT: Multilayer Graph Self-Attention Transformer',
            'authors': 'Keshav Singh, Mireille El geche, Pascal Frossard',
            'year': '2024',
            'venue': 'Researchgate'
        },
        {
            'title': 'Detection of resistive open and short defects in FDSOI under delay-based test: Optimal VDD and body biasing conditions',
            'authors': 'Amit Karel Florence Azais, Keshav Singh',
            'year': '2017',
            'venue': '2017 22nd IEEE European Test Symposium'
        }
    ]

    # Blogs
    blogs = [
        {
            'title': 'From Zero to Hero in GPU Performance Profiling & Optimization',
            'url': 'https://medium.com/@shaginhekvs/from-zero-to-hero-in-gpu-performance-profiling-optimization-e03da271ff18',
            'description': 'GPU performance optimization guide.'
        },
        {
            'title': 'First Nginx App Deployment Using K8s on Turing Pi Cluster',
            'url': 'https://medium.com/@shaginhekvs/first-nginx-app-deployment-using-k8s-on-turing-pi-cluster-8fb469ede6cd',
            'description': 'Kubernetes deployment tutorial.'
        },{
            'title': 'From Zero to (semi-)hero in MCP Toolbox for databases',
            'url': 'https://medium.com/@shaginhekvs/from-zero-to-semi-hero-in-mcp-toolbox-for-databases-2da802839fb6',
            'description': 'Enabling Agents to use MCP Toolbox for accessing databases.'
        }
    ]
    
    return render_template('index.html',
                         personal_info=personal_info,
                         summary=summary,
                         technical_skills=technical_skills,
                         experience=experience,
                         education=education,
                         projects=projects,
                         publications=publications,
                         blogs=blogs)

@app.route('/palantir-model-change')
def palantir_model_change():
    return render_template('palantir-model-change.html')


if __name__ == '__main__':
    app.run(debug=False)
