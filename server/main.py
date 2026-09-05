import os
import json
import time
from typing import List, Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="HireAI — Autonomous Voice & Code Technical Interviewer",
    version="1.0.0",
    description="Interactive AI Mock Interviewer simulating FAANG/Senior Engineering interviews with real-time feedback."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Supported Roles & Problem Bank
INTERVIEW_BANK = {
    "fullstack": [
        {
            "id": 1,
            "title": "Design a Distributed Rate Limiter (Token Bucket)",
            "difficulty": "Medium",
            "category": "System Design & Node.js",
            "prompt": "Explain how you would design an API rate limiter supporting 10,000 req/sec across multiple server instances using Redis. Write the token bucket algorithm in TypeScript/Python.",
            "starterCode": "function isRateLimited(userId: string, limit: number, windowSec: number): boolean {\n  // TODO: Implement sliding window or token bucket\n  return false;\n}"
        },
        {
            "id": 2,
            "title": "Two Sum & Optimization with Hash Map",
            "difficulty": "Easy-Medium",
            "category": "Algorithms",
            "prompt": "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target in O(N) time complexity.",
            "starterCode": "def two_sum(nums: list[int], target: int) -> list[int]:\n    # Implement O(N) solution using dict\n    pass"
        }
    ],
    "backend": [
        {
            "id": 3,
            "title": "PostgreSQL Concurrency & Row Locking (Deadlock Prevention)",
            "difficulty": "Hard",
            "category": "Database Engineering",
            "prompt": "You are handling concurrent financial transfers between two accounts. How do you prevent deadlocks when Account A transfers to B while B transfers to A simultaneously?",
            "starterCode": "async def transfer_funds(from_id: int, to_id: int, amount: float):\n    # Acquire locks in deterministic order\n    pass"
        }
    ],
    "ai_engineer": [
        {
            "id": 4,
            "title": "Implement RAG Chunking with Cosine Similarity",
            "difficulty": "Medium-Hard",
            "category": "AI / NLP",
            "prompt": "Write a vector search query function that computes cosine similarity between query embeddings and a set of document chunks in pure Python/NumPy.",
            "starterCode": "import numpy as np\n\ndef cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:\n    # Return cosine similarity\n    return 0.0"
        }
    ]
}

class EvaluateRequest(BaseModel):
    role: str
    problemId: int
    userCode: str
    spokenExplanation: Optional[str] = ""

class Scorecard(BaseModel):
    overallScore: int
    algorithmScore: int
    codeQualityScore: int
    communicationScore: int
    timeComplexity: str
    spaceComplexity: str
    strengths: List[str]
    areasToImprove: List[str]
    verdict: str

@app.get("/")
def root():
    return {
        "service": "HireAI Technical Interview Platform",
        "status": "OPERATIONAL",
        "supported_roles": list(INTERVIEW_BANK.keys()),
        "version": "1.0.0"
    }

@app.get("/api/problems/{role}")
def get_problems(role: str):
    problems = INTERVIEW_BANK.get(role.lower(), INTERVIEW_BANK["fullstack"])
    return {"role": role, "problems": problems}

@app.post("/api/evaluate", response_model=Scorecard)
def evaluate_submission(req: EvaluateRequest):
    # Analyze code length, structure, and explanation
    code = req.userCode.strip()
    explanation = req.spokenExplanation or ""

    if len(code) < 30:
        return Scorecard(
            overallScore=35,
            algorithmScore=30,
            codeQualityScore=40,
            communicationScore=45,
            timeComplexity="Unknown (Incomplete implementation)",
            spaceComplexity="Unknown",
            strengths=["Attempted initial structure"],
            areasToImprove=["Code is incomplete", "Missing core algorithmic logic", "Provide more verbal elaboration"],
            verdict="Needs Improvement / Did Not Pass"
        )

    # Heuristic AI Evaluator
    has_hash_map = "dict" in code or "{" in code or "Map" in code or "set" in code
    has_error_handling = "try" in code or "if" in code or "throw" in code or "raise" in code
    has_speech = len(explanation) > 15

    algo_score = 90 if has_hash_map else 75
    quality_score = 92 if has_error_handling else 80
    comm_score = 95 if has_speech else 70
    overall = int((algo_score * 0.4) + (quality_score * 0.3) + (comm_score * 0.3))

    verdict = "Strong Hire (Senior Level)" if overall >= 88 else "Hire (Mid Level)" if overall >= 75 else "Further Review Needed"

    return Scorecard(
        overallScore=overall,
        algorithmScore=algo_score,
        codeQualityScore=quality_score,
        communicationScore=comm_score,
        timeComplexity="O(N) Optimal" if has_hash_map else "O(N^2) Sub-optimal",
        spaceComplexity="O(N) Auxiliary Space",
        strengths=[
            "Clean idiomatic naming and clear function signatures",
            "Optimal data structure selection with instant lookup",
            "Proactive verbal articulation of trade-offs and edge cases"
        ],
        areasToImprove=[
            "Consider extreme boundary cases (e.g. integer overflow, empty array)",
            "Add automated unit test assertions at the end of the script"
        ],
        verdict=verdict
    )
