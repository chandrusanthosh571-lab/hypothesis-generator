import streamlit as st
import random
import time

def input_stage(topic):
    # Simply retrieves and passes the user topic
    return topic

def processing_stage(topic):
    # Normalizes text
    return topic.lower().strip()

def data_retrieval_stage():
    # Returns predefined dataset
    return [
        "exercise reduces obesity",
        "obesity increases diabetes risk",
        "sleep affects metabolism",
        "stress increases blood pressure",
        "junk food causes weight gain"
    ]

def filtering_stage(keyword, dataset):
    # Extracts relevant lines containing the keyword
    if not keyword:
        return []
    return [stmt for stmt in dataset if keyword in stmt.lower()]

def reasoning_stage(filtered_data):
    # Simulates analyzing relationships between filtered data
    return len(filtered_data) > 0

def hypothesis_generation_stage(topic, filtered_data):
    # Logic to formulate hypothesis based on result count
    if len(filtered_data) >= 2:
        return f"If {filtered_data[0]} and {filtered_data[1]}, they form a linked mechanism."
    elif len(filtered_data) == 1:
        return f"It is hypothesized that {filtered_data[0]}."
    else:
        return f"'{topic}' may be related to unknown factors."

def evidence_stage(filtered_data):
    # Returns related lines
    return filtered_data

def output_stage(hypothesis, evidence):
    # Displays results in the UI
    st.success("Hypothesis Generated Successfully ✅")
    
    st.subheader("💡 Hypothesis")
    st.info(hypothesis)
    
    st.subheader("📊 Evidence")
    if evidence:
        for ev in evidence:
            st.markdown(f"- {ev.capitalize()}")
    else:
        st.markdown("- *No direct evidence found.*")
    
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🔬 Method")
        st.write("Data Analysis")
        
    with col2:
        st.subheader("✅ Feasibility")
        st.write("High")
        
    with col3:
        st.subheader("📈 Confidence Score")
        confidence = random.randint(70, 95)
        st.metric(label="", value=f"{confidence}%")

def main():
    st.set_page_config(page_title="AI Research Hypothesis Generator", layout="centered")
    
    st.title("🔬 AI Research Hypothesis Generator")
    st.write("Enter a topic below to simulate an intelligent agent generating a research hypothesis.")
    st.markdown("---")
    
    user_topic = st.text_input("Enter a research topic (e.g., obesity, sleep, stress):")
    
    if st.button("Generate"):
        if user_topic:
            with st.spinner("Agent is running workflow..."):
                time.sleep(0.5) # Slight pause to simulate processing time
                
                # Execute agent workflow stages
                topic = input_stage(user_topic)
                keyword = processing_stage(topic)
                dataset = data_retrieval_stage()
                filtered_data = filtering_stage(keyword, dataset)
                has_relations = reasoning_stage(filtered_data)
                hypothesis = hypothesis_generation_stage(topic, filtered_data)
                evidence = evidence_stage(filtered_data)
                
                # Display step-by-step workflow using expanders
                with st.expander("🔍 View Agent Workflow Steps", expanded=False):
                    st.markdown(f"**1. Input Stage:** Received user topic '{topic}'")
                    st.markdown(f"**2. Processing Stage:** Normalized input to '{keyword}'")
                    st.markdown(f"**3. Data Retrieval Stage:** Searched predefined dataset ({len(dataset)} items)")
                    st.markdown(f"**4. Filtering Stage:** Found {len(filtered_data)} relevant matches")
                    st.markdown(f"**5. Reasoning Stage:** Identified {'relationships' if has_relations else 'no direct relationships'}")
                    st.markdown(f"**6. Hypothesis Generation Stage:** Synthesized hypothesis")
                    st.markdown(f"**7. Evidence Stage:** Extracted supporting details")
                    st.markdown(f"**8. Output Stage:** Displaying results in UI")
                
                # Output stage results display
                output_stage(hypothesis, evidence)
        else:
            st.warning("Please enter a research topic to proceed.")

if __name__ == "__main__":
    main()