from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import todo_state

class TodoItem(AdditionalDataHolder, Parsable):
    """
    A task that needs to be completed
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def completed_date(self,) -> Optional[datetime]:
        """
        Gets the completedDate property value. The completedDate property
        Returns: Optional[datetime]
        """
        return self._completed_date
    
    @completed_date.setter
    def completed_date(self,value: Optional[datetime] = None) -> None:
        """
        Sets the completedDate property value. The completedDate property
        Args:
            value: Value to set for the completedDate property.
        """
        self._completed_date = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new TodoItem and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The completedDate property
        self._completed_date: Optional[datetime] = None
        # The description property
        self._description: Optional[str] = None
        # The dueDate property
        self._due_date: Optional[datetime] = None
        # The id property
        self._id: Optional[str] = None
        # The listId property
        self._list_id: Optional[str] = None
        # The name property
        self._name: Optional[str] = None
        # The state property
        self._state: Optional[todo_state.TodoState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TodoItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TodoItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TodoItem()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description property
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description property
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def due_date(self,) -> Optional[datetime]:
        """
        Gets the dueDate property value. The dueDate property
        Returns: Optional[datetime]
        """
        return self._due_date
    
    @due_date.setter
    def due_date(self,value: Optional[datetime] = None) -> None:
        """
        Sets the dueDate property value. The dueDate property
        Args:
            value: Value to set for the dueDate property.
        """
        self._due_date = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "completed_date": lambda n : setattr(self, 'completed_date', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "due_date": lambda n : setattr(self, 'due_date', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "list_id": lambda n : setattr(self, 'list_id', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(todo_state.TodoState)),
        }
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. The id property
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. The id property
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
    @property
    def list_id(self,) -> Optional[str]:
        """
        Gets the listId property value. The listId property
        Returns: Optional[str]
        """
        return self._list_id
    
    @list_id.setter
    def list_id(self,value: Optional[str] = None) -> None:
        """
        Sets the listId property value. The listId property
        Args:
            value: Value to set for the listId property.
        """
        self._list_id = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name property
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name property
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_datetime_value("completedDate", self.completed_date)
        writer.write_str_value("description", self.description)
        writer.write_datetime_value("dueDate", self.due_date)
        writer.write_str_value("id", self.id)
        writer.write_str_value("listId", self.list_id)
        writer.write_str_value("name", self.name)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def state(self,) -> Optional[todo_state.TodoState]:
        """
        Gets the state property value. The state property
        Returns: Optional[todo_state.TodoState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[todo_state.TodoState] = None) -> None:
        """
        Sets the state property value. The state property
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    

