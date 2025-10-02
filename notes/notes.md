# Generative AI using LangChain

## 3. Chains in LangChain
1. **Chains:** 
   A chain is basically a pipeline of components in LangChain where the output of one component is passed as input to the next.
    ```nginx
    Prompt → Model → Parser
    ```
    So, you can think of a Chain as:
   - Input → [Sequence of steps] → Output

2. **Chain Definition:**
    ```nginx
        chain = prompt | model | parser
    ```
    The | operator means “pipe the output into the next component.”
    ![alt text](image.png)
    ```lua
        +-------------+       
        | PromptInput |       
        +-------------+       
                *              
                *              
                *              
        +----------------+     
        | PromptTemplate |     
        +----------------+     
                *              
                *              
                *              
          +-----------+        
          | OllamaLLM |        
          +-----------+        
                *              
                *              
                *              
       +-----------------+     
       | StrOutputParser |     
       +-----------------+     
                *              
                *              
                *              
     +-----------------------+  
     | StrOutputParserOutput |  
     +-----------------------+ 
    ```