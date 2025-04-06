def combine_tokens(ner_output):
    results = []
    current_entity = None

    for token in ner_output:
        #print(token)
        entity_type = token["entity"].split("-")[-1]
        word = token["word"].replace("##", "")

        if token["entity"].startswith("B-") or current_entity is None or current_entity["entity"] != entity_type:
            # Start of new entity
            if current_entity:
                results.append(current_entity)
            current_entity = {
                "entity": entity_type,
                "value": word,
                "start": token["start"],
                "end": token["end"]
            }
        else:
            # Continuation of current entity
            if token["word"].startswith("##"):
              # token is part of the same word
              current_entity["value"] += word
            else:
              current_entity["value"] += " " + word
            current_entity["end"] = token["end"]

    # Append the last entity
    if current_entity:
        results.append(current_entity)

    return results

def humanize_tag(tag):
  match tag:
    case "PER":
      return "Person"
    case "ORG":
      return "Organization"
    case "LOC":
      return "Location"
    case "_":
      return tag


def tag_text(text, tags):
    for tag in tags:
        entity = tag["entity"]
        value = tag["value"]

        # Replace the text with the tagged version
        text = text.replace(value, f"<span class='{entity} entity' alt='{entity}' title='{humanize_tag(entity)}'>{value}</span>")

    return text