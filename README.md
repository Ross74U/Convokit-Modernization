# RealTime Transcriptional Understanding Framework

## Overview

This project develops a middle-ground approach to conversational understanding that balances performance with flexibility. We compare traditional conversational analysis frameworks with modern LLM approaches and propose a more efficient SBERT-based solution for real-time applications.

## Table of Contents
- [Current Approaches](#current-approaches)
  - [Convokit Framework](#convokit-framework)
  - [LLM-based Approaches](#llm-based-approaches)
- [Our Proposal: SBERT-based Transformer](#our-proposal-sbert-based-transformer)
- [Performance Benchmarks](#performance-benchmarks)
- [Current Research](#current-research)
- [Implementation Examples](#implementation-examples)

## Current Approaches

We've identified two extremes in the current landscape:

### Convokit Framework

[Convokit](https://convokit.cornell.edu/documentation/featureExtraction.html) is specifically built for conversation analysis and large-scale corpus processing, generally predating modern LLMs and sentence transformers.

**Available Techniques:**
- Bag-of-words
- Column-normalized tf-idf
- Hyperconvo
- PhrasingMotifs
- PolitenessStrategies
- PromptTypes
- ExpectedContextModel*

#### ExpectedContextModel Deep Dive
This approach is based on contextual understanding of utterances:
- Uses LSA approach combined with SVD dimension reduction
- Models utterances based on their conversational context (replies and predecessors)
- Embeds terms and utterances in a latent "context space" where proximity indicates similarity in expected conversational role/function
- Creates shared vector space for terms, utterances and contexts through SVD

**Strengths:** Excellent for specific tasks (understanding redirection in SCOTUS proceedings, therapy conversations, etc.) where conversational flow outweighs semantics; highly performant for large corpus analysis.

**Limitations:** Lacks versatility; requires domain-specific adaptations.

### LLM-based Approaches

The other extreme uses large language models with prompt engineering:

- Relies on centralized LLM APIs (OpenAI, Anthropic, Google, etc.)
- Examples in production:
  - Telephone agents for client information (Swartz center)
  - Social media comment analysis/filtering

**Strengths:** Highly general and adaptable.

**Limitations:** High resource consumption, centralized dependency, high latency.

## Our Proposal: SBERT-based Transformer

We propose a sentence-BERT based approach that offers:

- General adaptability to many conversational understanding scenarios
  - Bidirectional context understanding
  - Semantic and topic relation understanding
- Much higher performance than LLM prompt engineering
  - Distributable computation (can run on personal computers)
  - Suitable for decentralized applications
- Higher quality and adaptability than traditional Convokit methods

## Performance Benchmarks

1. **Convokit Framework (ExpectedContextModel)**
   - Expected Latency: ~10-50ms per utterance
   - Factors: LSA + SVD computation (lightweight), no deep learning, reusable embeddings

2. **LLM Prompt Engineering Approach**
   - Expected Latency: ~500-2000ms per utterance
   - Factors: API calls, network latency, large model inference, token overhead

3. **SBERT-based Transformer**
   - Expected Latency: ~50-200ms per utterance
   - Factors: Local computation, optimized for sentence embeddings, GPU acceleration

Testing conditions:
- Hardware: SBERT on Nvidia RTX 5000 (12GB VRAM), LSA on Intel i7-9750H
- LLM baseline: OpenAI API with GPT-3.5 Turbo Instructor (200 token limit)
- Average utterance: 20-50 words
- Single utterance processing (non-batched)

## Current Research

We are currently evaluating the SBERT approach against Convokit on its home turf:
- Expected context modeling
- Predicted conversational flow
- Redirection detection
- Using original Convokit corpuses for fair comparison

## Next Steps

Evaluation of the SBERT approach against naive LLM prompt engineering.

## Implementation Examples

### Parliamentary Question Period Analysis

**Traditional Convokit approach:**
- Uses only question verbs, discarding surrounding text and nouns
- Applies Tdf → LSA for global utterance clustering
- Models forward context (answers not necessary for our application)

**Our SBERT implementation plan:**
- Global transform with similar clustering but reduced dimensions to better capture topic-term relations
- Implement same forward context modeling within Expected Conversational Context Framework
- Perform comparative analysis on government versus non-governmental question types

## References

- [Convokit Documentation](https://convokit.cornell.edu/documentation/featureExtraction.html)
- [Parliament Demo Analysis](https://github.com/CornellNLP/ConvoKit/blob/master/convokit/expected_context_framework/demos/parliament_demo.ipynb)

