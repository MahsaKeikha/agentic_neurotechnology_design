def design_gate(context): return {"allowed": not context.get("request_clinical_authorization",False),"requires_human_review":True}
