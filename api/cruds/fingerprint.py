from typing import Optional, Tuple

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import Session

import api.models.fingerprint as fp_model
import api.schemas.fingerprint as fp_schema


def create_fingerprint(db: Session, create_request: fp_schema.FingerprintRegisterRequest) -> fp_model.FingerPrint:
    fingerprint: fp_model.FingerPrint = fp_model.FingerPrint(
        token=create_request.token,
        registration_device=create_request.registration_device,
        place=create_request.place,
        characteristics=create_request.characteristics,
        hash=create_request.hash
    )

    db.add(fingerprint)

    db.commit()
    db.refresh(fingerprint)

    return fingerprint


def get_finger_print_by_id(db: Session, uuid: str) -> Optional[fp_model.FingerPrint]:
    result: Result = db.execute(
        select(fp_model.FingerPrint).filter(fp_model.FingerPrint.id == uuid)
    )

    fingerprints: Optional[Tuple[fp_model.FingerPrint]] = result.first()

    first: Optional[fp_model.FingerPrint] = None

    # 要素が一つであってもtupleで返却されるので１つ目の要素を取り出す
    if fingerprints is not None:
        first: Optional[fp_model.FingerPrint] = fingerprints[0]

    return first
