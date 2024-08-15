import streamlit as st
import helper_functions as hlpr_func

def main():
    st.set_page_config(
        page_title="CodeGenie",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    with open("./css/theme.txt", "r") as css_file:
        css = css_file.read()

    css_styling=f"""{css}"""
    st.markdown(css_styling, unsafe_allow_html=True)

    st.markdown("<h1 style='display: block; color: #b0b0b0; text-align: center;'>CodeGenie: An AI Wizard</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='display: block; color: #e7e7e7; text-align: center;'>Magically Generate, Execute, and Debug Python Code with One Click!</h5>", unsafe_allow_html=True)

    user_prompt = st.text_area("Enter your Python code prompt:", "Write a Python function that reads the file in a given directory and then returns the head of csv.")

    if st.button("Generate Code"):
        with st.spinner('Generating code...'):
            generated_code = hlpr_func.generate_code(user_prompt)
        st.session_state.generated_code = generated_code
        st.session_state.user_inputs = {}
        st.session_state.code_with_inputs = ""

    if 'generated_code' in st.session_state:
        st.subheader("Generated Code:")
        st.code(st.session_state.generated_code, language='python')

        parameters = hlpr_func.extract_function_parameters(st.session_state.generated_code)

        if parameters:
            st.subheader("Enter Values for Inputs:")
            st.session_state.user_inputs = hlpr_func.render_input_fields(parameters)

        if st.button("Execute Code"):
            if all(value.strip() != "" for value in st.session_state.user_inputs.values()):
                with st.spinner('Preparing code for execution...'):
                    st.session_state.code_with_inputs = hlpr_func.prepare_code_for_execution(st.session_state.generated_code, st.session_state.user_inputs)
                st.subheader("Code with Inputs:")
                st.code(st.session_state.code_with_inputs, language='python')
                
                retry_attempts = 5
                for attempt in range(retry_attempts):
                    with st.spinner(f'Executing code (Attempt {attempt + 1})...'):
                        success, output = hlpr_func.execute_code(st.session_state.code_with_inputs, timeout=100 * (attempt + 1))

                    execution_result, message = hlpr_func.determine_execution_success(output, st.session_state.user_inputs)

                    if execution_result == "Success":
                        st.subheader("Code Executed Successfully:")
                        st.text(message)
                        st.success("Task completed successfully!")
                        break
                    else:
                        st.error(f"Error occurred:\n{message}")
                        if "ModuleNotFoundError" in message:
                            hlpr_func.handle_missing_modules(message)
                        if attempt < retry_attempts - 1:  # Only fix and retry if it's not the last attempt
                            with st.spinner('Fixing code...'):
                                st.session_state.code_with_inputs = hlpr_func.fix_code(st.session_state.code_with_inputs, message)
                            st.subheader("Fixed Code:")
                            st.code(st.session_state.code_with_inputs, language='python')
                
                if execution_result != "Success":  # If all attempts failed
                    st.warning("Maximum retry attempts reached without success.")
            else:
                st.error("Please provide all required inputs before executing the code.")

if __name__ == "__main__":
    main()